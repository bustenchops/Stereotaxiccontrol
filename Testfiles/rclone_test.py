import os


def copy_folder_from_onedrive():
    result = os.system('rclone copy onedrive:scans D:/aa')



copy_folder_from_onedrive()