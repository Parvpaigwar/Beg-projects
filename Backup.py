import os
import shutil
import datetime
import schedule
import time

source_dir = r"C:\Users\parvp\OneDrive\Pictures\Screenshots"
destination_dir = r"C:\Users\parvp\OneDrive\Desktop\Backup"

def copy_folder_to_dir(source,dest):
    today = datetime.datetime.today()
    dest_dir = os.path.join(dest, str(today).replace(':', '-'))

    try:
        shutil.copytree(source, dest_dir)
        print(f"Floder copied to : {dest_dir}")
    except FileExistsError:
        print(f"folder already exist in : {dest}")

schedule.every().day.at("18:57").do(lambda : copy_folder_to_dir(source_dir,destination_dir))

while True:
    schedule.run_pending()
    time.sleep(60)