# L3 Dumper

Script to dump L3 CDM from any rooted Android device.

## Things to remember

Does not work on Android 11+. On other Android versions you need to check your device Widevine CDM (to check use application [DRM Info](https://play.google.com/store/apps/details?id=com.androidfung.drminfo)). Make sure OEM Crypto API version is 13 or less. Make sure Security Level is L3. If it's L1, you need to install a Magisk module called [liboemcrypto-disabler](https://github.com/umylive/liboemcrypto-disabler).

## Usage

* Download and install [Python 3.9.0](https://www.python.org/downloads/release/python-390/).
* Install required Python 3.9.0 dependencies using command:
`pip3 install -r requirements.txt`
* Download and install [Frida Server](https://play.google.com/store/apps/details?id=me.shingle.fridaserver) application from Google Play store and start the server.
* Enable USB debugging on your Android device and connect it to your computer.
* Execute the script using command:
`python3 dump_keys.py`

After successful run you will have a new folder `key_dumps` with needed keys inside.

## Only getting key_boxes?

Private key dump is possible, you need to modify `script.js` to include the `KNOWN_DYNAMIC_FUNC` for your Android device.

## Credits

Thanks to the original author of the code.
