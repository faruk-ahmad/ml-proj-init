"""
A module for validatinig different parameters given by user
"""

import os
import string
import sys

# import configs
from .config import configs

class Validation():
    """
    A class holding required methods for validating user inputs
    """

    def __init__(self):
        self.valid_choice_run_mode = configs["run_name_choices"]
        self.proj_name_first_char = configs["proj_name_first_char"]
        self.proj_name_rest_part = configs["proj_name_allowed_char"]
        self.proj_name_length = configs["proj_name_length"]
        self.valid_project_type = configs["valid_proj_type"]


    def is_valid_mode(self, run_mode):
        """
        Method for validating user input for run mode
        """
        try:
            if run_mode in self.valid_choice_run_mode:
                return True
            else:
                return False
        except Exception as e:
            #print(f"Invalid run mode")
            return False
        else:
            return True

    def is_valid_project_name(self, proj_name):
        """
        Method for validating user input for project name
        """
        try:
            if proj_name is not None and len(proj_name) >= 1:
                first_char = proj_name[0]

                if len(proj_name) <= self.proj_name_length:
                    if first_char in self.proj_name_first_char:
                        if all(ch in self.proj_name_rest_part for ch in proj_name):
                            return True
                        return False
                    return False
                return False
            else:
                #print(f"None type in project name")
                return False
        except Exception as e:
            #print(f"Invalid project nmae")
            return False
        else:
            return True

    def is_valid_path(self, proj_path):
        """
        Method for validating user input for project path
        """
        try:
            if os.path.isdir(proj_path):
                return True
            return False
        except Exception as e:
            #print(f"Invalid project path")
            return False
        else:
            return True

    def is_path_exists(self, proj_dir):
        """
        Method to check if project directory already exists, if exists prompt to delete the existing directory
        """
        try:
            if os.path.exists(proj_dir) and os.path.isdir(proj_dir):
                return True
            return False
        except Exception as e:
            #print("Invalid project dir")
            return False
        else:
            return True