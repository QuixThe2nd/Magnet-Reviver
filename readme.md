# Magnet Reviver
Magnet Reviver is a script that automatically converts magnet links to torrent files.

## How it Works
Magnet Reviver automatically checks torrent caching sites to see if they have stored a copy of the torrent file for that infohash.

## Future Improvements
I wrote this script up real quick just to simplify my life a little, I don't plan on updating it. If you'd like to improve the script, feel free to fork and PR.

### Auto Captcha
btcache has a captcha, the script is able to check if btcache has the torrent file, but doesn't automate captcha

### Improved Torrage Decryption
Torrage uses a basic Caesar Shift "encryption" algorithm to try prevent automations like this. I've unobfuscated/deobfuscated the decryption algorithm, but in my testing, it only works half the time.

### Native Torrent Generation
Right now the script scrapes torrent files off existing caches. The script could be improved by implementing the torrent protocol natively; retreiving torrent metadata from peers to generate the torrent file.

### Unified Output
Currently the script outputs links to download the torrent file. If Torrage decryption or native torrent generation is built, the script will need to be rewritten to download torrent files from the URLs and output them directly.
