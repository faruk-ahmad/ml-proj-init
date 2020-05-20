"""
A utility module for performing some utility task to initialize ml or dl projects
"""

import os
import sys
import shutil


from .config import configs
from .validation import Validation

class Utility():
    """
    A class that holds necessary methods for some utility tasks
    """

    def __init__(self):
        self.ml_template_path = configs["ml_template_path"]
        self.dl_template_path = configs["dl_template_path"]
        self.data_loader_path = configs["data_loader_path"]
        self.network_template_path = configs["network_template_path"]

        self.val = Validation()


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
                print(f"Exception occurred in creaing ml project structure.. {e}")
                return False
            else:
                return True 
        
        if proj_type == "dl":
            try:
                print(f"Creating DL project structure...")
                shutil.copytree(self.dl_template_path, proj_dir)
            except Exception as e:
                print(f"Exception occurred in creating dl project structure.. {e}")
                return False
            else:
                return True


    def append_data_loader(self, project_path, data_loader_type):
        """
        Method to append data loader to existing project
        """
        try:
            print(f"appending data loader..")
            copy_path = os.path.join(project_path, "src")

            # lets check if the path exists, if not lets create the src directory
            if not self.val.is_path_exists(copy_path):
                # create the directory
                os.makedirs(copy_path)
            
            where_to_copy = os.path.join(copy_path, data_loader_type + "_loader.py")
            file_to_copy = os.path.join(self.data_loader_path, data_loader_type + "_loader.py")

            shutil.copyfile(file_to_copy, where_to_copy)
        except Exception as e:
            print(f"Exception occurred in dataloader adding. {e}")
            return False
        else:
            return True



    def append_network_architecture(self, project_path, network_architecture_type):
        """
        Method to append network architecture to existing project
        """
        try:
            print(f"appending network architecture..")
            copy_path = os.path.join(project_path, "src")

            # lets check if the path exists, if not lets create the src directory
            if not self.val.is_path_exists(copy_path):
                # create the directory
                os.makedirs(copy_path)
            
            where_to_copy = os.path.join(copy_path, network_architecture_type + "_nn.py")
            file_to_copy = os.path.join(self.network_template_path, network_architecture_type + "_nn.py")

            shutil.copyfile(file_to_copy, where_to_copy)
        except Exception as e:
            print(f"Exception occurred in network architecture adding. {e}")
            return False
        else:
            return True