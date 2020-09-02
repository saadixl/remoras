# Disclaimer!
- This is project is completely for learning purpose and understanding the security vulnerabilities of using USB drives in public computers
- Tried it only on RaspbianOS. Might not work on other OS
- Remoras is kind of a suckerfish

## How to use it?
- Clone this project
- Go inside `config.py` file
- Set the download location of copied file from USB: `/home/YOUR_USER_NAME/path/to/your/chosen/directory`
- Set the mount point of USB drive:  `/media/YOUR_USER_NAME`
- Once config is set, make the `sucker.sh` executable by running the following command:
-  `chmod +x sucker.sh`
-  Now run the `remoras.py` like `python3 remoras.py` or you can use [pm2](https://www.npmjs.com/package/pm2) to keep it running
-  So the `remoras.py` will keep running every second
-  Once you insert a USB drive, it will take 5 second to let the drive mount properly and then it will copy the whole drive under the location you set on `config.py` under a timestamped folder