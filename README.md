# Dumper

Dumper is a Frida script to dump L3 CDMs from any Android device. Root needed.

## Usage

* Download [ADB](https://developer.android.com/studio/releases/platform-tools) and have it ready to use.
* Download and install Python 3.9.0.
* Install required Python 3.9.0 dependencies:
`pip3 install -r requirements.txt`
* Download and install ["Frida Server"](https://play.google.com/store/apps/details?id=me.shingle.fridaserver) application from Google Play store and start the server.
* Enable USB debugging on your Android device and connect it to your computer.
* After connecting verify your device is connected:
`adb devices`
* Execute dump_keys.py:
`python3 dump_keys.py`

## Temporary disabling L1 to use L3 instead
A few phone brands let us use the L1 keybox even after unlocking the bootloader (like Xiaomi). In this case, installation of a Magisk module called [liboemcrypto-disabler](https://github.com/umylive/liboemcrypto-disabler) is necessary.

## Known issues
It seems like Google made some changes in their OEMCrypto library and it broke the script. Further investigation is needed to make it work on Android 11+, feel free to open PRs.

## Credits
Thanks to the original author of the code.
