"""
A utility module for performing some utility task to initialize ml or dl projects
"""

import os
import sys
import shutil

from config import config

class Utility():
    """
    A class that holds necessary methods for some utility tasks
    """

    def __init__(self):
        self.ml_template_path = config["ml_template_path"]
        self.dl_template_path = config["dl_template_path"]


    def get_user_consent(self):
        """
        Method to prompt for deletion and get user consent
        """
        print("Path already exists, do you want to delete it?")

        consent = input("Y/N: ").lower()

        return consent

    def delete_existing_path(self, proj_dir):
        """
        Method to try to delete existing path based on user consent
        """
        try:
            shutil.rmtree(proj_dir)
        except Exception as e:
            print("Path not writable, can not delete directory.")
            return False
        else:
            return True

    
    def create_project_structure(self, proj_type, proj_dir):
        """
        Method to create ML project structure
        """
        if proj_type == "ml":
            try:
                print(f"Creating ML project structure...")
                shutil.copytree(self.ml_template_path, proj_dir)
            except Exception as e:
                print(f"Exception occurred. {e}")
                return False
            else:
                return True 
        
        if proj_type == "dl":
            try:
                print(f"Creating DL project structure...")
                shutil.copytree(self.dl_template_path, proj_dir)
            except Exception as e:
                print(f"Exception occurred. {e}")
                return False
            else:
                return True
