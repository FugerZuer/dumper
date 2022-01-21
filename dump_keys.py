#!/usr/bin/env python3

import os
import time
import frida
import logging
from Helpers.Scanner import Scan

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(lineno)d - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %I:%M:%S %p',
    level=logging.DEBUG,
)

device = frida.get_usb_device()
scanner = Scan(device.name)
logging.info(f'Connected to {device.name}')
choice = input("Do you want to launch DRM content on Chrome (y/n)? ")
if choice.lower() == "y":
    os.system('adb shell am start -n com.android.chrome/org.chromium.chrome.browser.ChromeTabbedActivity -d "https://bitmovin.com/demos/drm"')
logging.info('Scanning all processes for the following libraries')
for process in device.enumerate_processes():
    logging.debug(process)
    if 'drm' in process.name:
        libraries = scanner.find_widevine_process(device, process.name)
        if libraries:
            for library in libraries:
                scanner.hook_to_process(device, process.name, library)
logging.info('Hooks completed')
while True:
    time.sleep(1000)
