"""
A utility module for performing some utility task to initialize ml or dl projects
"""

import os
import sys
import shutil

class Utility():
    """
    A class that holds necessary methods for some utility tasks
    """

    def __init__(self):
        pass


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

    
    def create_ml_project_structure(self):
        """
        Method to create ML project structure
        """
        pass