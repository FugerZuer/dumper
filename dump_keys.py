#!/usr/bin/env python3

import os
import time
import frida
import logging
import platform
import subprocess
from Helpers.Scanner import Scan

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(lineno)d - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %I:%M:%S %p',
    level=logging.DEBUG,
)

logging.addLevelName( logging.ERROR, "\033[1;31m%s\033[1;0m" % logging.getLevelName(logging.ERROR))
logging.addLevelName( logging.INFO, "\033[1;33m%s\033[1;0m" % logging.getLevelName(logging.INFO))
logging.addLevelName( logging.DEBUG, "\033[1;34m%s\033[1;0m" % logging.getLevelName(logging.DEBUG))

if platform.system() == "Windows":
	adb_location = os.path.dirname(os.path.realpath(__file__))+"\\Tools\\adb.exe"
	fastboot_location = os.path.dirname(os.path.realpath(__file__))+"\\Tools\\fastboot.exe"
else:
	adb_location = "adb"
	fastboot_location = "fastboot"

output = subprocess.run(adb_location+' devices', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode('utf-8')
output = output.split("\n")
for text in output:
	if text != "" and text != "\r":
		logging.info(text)
print()
try:
	device = frida.get_usb_device()
except frida.InvalidArgumentError as err:
	if "device not found" in str(err):
		logging.error("No devices. Please connect your Android device.")
	else:
		logging.error(err)
	exit()
scanner = Scan(device.name)
logging.info(f'Connected to {device.name}')
logging.info('Do you want to launch DRM content on Chrome (y/n)?')
choice = input("")
if choice.lower() == "y":
	output = subprocess.run(adb_location+' shell am start -n com.android.chrome/org.chromium.chrome.browser.ChromeTabbedActivity -d "https://bitmovin.com/demos/drm"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode('utf-8')
	output = output.split("\n")
	for text in output:
		if text != "" and text != "\r":
			logging.debug(text)
logging.info('Scanning all processes for the following libraries')
try:
	for process in device.enumerate_processes():
		logging.debug(process)
		if 'drm' in process.name:
			libraries = scanner.find_widevine_process(device, process.name)
			if libraries:
				for library in libraries:
					scanner.hook_to_process(device, process.name, library)
except frida.ServerNotRunningError as err:
	if "unable to connect to remote frida-server: closed" in str(err):
		logging.error("Frida Server is not running on the Android Device.")
	else:
		logging.error(err)
	exit()
logging.info('Hooks completed')
while True:
    time.sleep(1000)
