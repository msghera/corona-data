from datetime import datetime
import os

class FileManager:
    def __init__(self):
        self.foldername = str(datetime.now().timestamp()).split('.')[0]
        self.BASE_DIR = os.getcwd()
        self.BASE_DATA_DIR = "{}/data".format(self.BASE_DIR)
        self.BASE_FOLDER_DIR = "{}/data/{}".format(self.BASE_DIR, self.foldername)

        self.create_folder()

    def create_data_folder(self):
        try:
            os.mkdir(self.BASE_DATA_DIR)
        except OSError:
            print("Failed to create data folder. Check permission for user.")
        else:
            print("Data folder is created successfully. Path is {}".format(self.BASE_DATA_DIR))


    def create_folder(self):
        if not os.path.exists(self.BASE_DATA_DIR):
            self.create_data_folder()
        try:
            os.mkdir(self.BASE_FOLDER_DIR)
        except OSError:
            print("Failed to create folder. Check permission for user.")
        else:
            print("Timestamp folder is created successfully. Path is {}".format(self.BASE_FOLDER_DIR))


    def get_folder_dir(self):
        return self.BASE_FOLDER_DIR