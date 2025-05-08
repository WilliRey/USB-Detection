import psutil
import time
import logging

logging.basicConfig(filename='usb_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def get_current_drives():
    return set(part.device for part in psutil.disk_partitions())

def main():
    known_drives = get_current_drives()
    print("Monitoring for new drives...")

    while True:
        current_drives = get_current_drives()
        new_drives = current_drives - known_drives

        for drive in new_drives:
            logging.info(f"New drive detected: {drive}")
            print(f"New drive detected: {drive}")

        known_drives = current_drives
        time.sleep(5)

if __name__ == "__main__":
    main()
