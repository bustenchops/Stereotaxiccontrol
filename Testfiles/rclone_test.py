import subprocess


def copy_folder_from_onedrive():
    """
    Copies a folder from OneDrive to a local directory using rclone.

    :param remote_name: The name of the remote configured in rclone (e.g., 'onedrive')
    :param remote_path: The path to the folder in OneDrive (e.g., 'Documents/FolderName')
    :param local_path: The local path where the folder should be copied (e.g., '/path/to/local/folder')
    """
    try:
        # Construct the rclone copy command

        # Execute the command
        result = subprocess.run(rclone copy onedrive:'Active Folder/expense D:\aa', check=True, capture_output=True, text=True)

        # Print the output
        print("Output:", result.stdout)
        print("Error:", result.stderr)
        print("Folder copied successfully!")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        print("Output:", e.stdout)
        print("Error:", e.stderr)



copy_folder_from_onedrive()