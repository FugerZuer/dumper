# L3 Dumper

Script to dump L3 CDM from any rooted Android phone.

## Things to remember

Does not work on Android 11+. On lower Android version you need to check your device Widevine Security Level (to check use application [DRM Info](https://play.google.com/store/apps/details?id=com.androidfung.drminfo)). Make sure Security Level is L3. If it's L1, you need to install a Magisk module called [liboemcrypto-disabler](https://github.com/umylive/liboemcrypto-disabler).

## Usage

* Download [ADB](https://developer.android.com/studio/releases/platform-tools) and have it ready to use.
* Download and install Python 3.9.0.
* Install required Python 3.9.0 dependencies:
`pip3 install -r requirements.txt`
* Download and install [Frida Server](https://play.google.com/store/apps/details?id=me.shingle.fridaserver) application from Google Play store and start the server.
* Enable USB debugging on your Android device and connect it to your computer.
* After connecting verify your device is connected:
`adb devices`
* Execute the script:
`python3 dump_keys.py`

After successful run you will have a new folder `key_dumps` with needed keys inside.

## Credits

Thanks to the original author of the code.
