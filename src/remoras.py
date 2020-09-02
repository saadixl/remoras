import subprocess
import time
import re
import config

def get_drive_names():
    s = str(subprocess.check_output("lsblk"))
    s = s.strip()
    return re.findall(r"sd.[0-9]", s)

expect_new_device = 1

while True:
    drive_names = get_drive_names()
    d_len = len(drive_names)
    if d_len == 0:
        expect_new_device = 1
        print("No drive name found on the list. Retrying in 1s")
    else:
        if expect_new_device == 1:
            for dname in drive_names:
                if dname is not None:
                    print("Found {} drives, ready for copying".format(d_len))
                    subprocess.run(["./sucker.sh", config.download_location, config.drive_mount_point])
                    print("Copying data from drive...")
                    expect_new_device = 0
    time.sleep(1)
