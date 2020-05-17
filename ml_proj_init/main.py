"""
the main module of ml-proj-init library
"""

import os
import sys
import argparse

# import required classes
from ml_proj_init.utils import Utility
from ml_proj_init.validation import Validation


"""
start method for ml-project-init python lib
"""

def start():
    # first create the argument parser
    ml_proj_parser = argparse.ArgumentParser(
                                            prog="ML-PROJ-INIT",
                                            usage="%(prog)s [options]",
                                            description="Arguments for initializing machine learning and deep learning project",
                                            epilog="A good project structure is the first step to a good project. Enjoy! :)"
                                            )

    # lets add the necessary arguments

    """
    -m or --mode: Mode of running the lib, c for creation mode, a for append mode
    type: only string type value is accepted
    choices: only two options are available
    help: help text for the argument
    required: Users are forced to apply this argument
    default: Default value is c, that is the creation mode.
    """
    ml_proj_parser.add_argument(
                                "-m",
                                "--mode",
                                type=str,
                                choices=["c", "a"],
                                help="Mode to run ml-proj-init to create or append project structure.",
                                required=True,
                                default="c"
                                )

    """
    -n or --name: Name of the project to create project structure
    type: only string type of value is accepted
    help: help string for the argument
    required: True, the user is forced to provide the arugment to get the lib worked
    """
    ml_proj_parser.add_argument(
                                "-n",
                                "--name",
                                type=str,
                                help="Project name to initialize the project.",
                                required=True
                                )

    """
    -p or --path: Path for creating the project structure
    type: only string type of value is accepted
    help: help string for the argument
    required: Flase, the argument is option, if path is not given, the project will be created in the current location
    """
    ml_proj_parser.add_argument(
                                "-p",
                                "--path",
                                type=str,
                                help="A valid path to create the project stucture.",
                                required=False
                                )
    
    """
    -t or --type: Type of the project, generic machine learning project or deep learning project
    type: only one of the string value from choicese will be accepted
    help: help string for the argument
    choices: the user are forced to pick one of the given values
    default: if user does not provide any values, then default will be used.
    """
    ml_proj_parser.add_argument(
                                "-t",
                                "--type",
                                type=str,
                                help="Type of project to create project structure.",
                                choices=["ml", "dl"],
                                default="ml"
                                )

    ml_proj_args = ml_proj_parser.parse_args()
    print(ml_proj_args)


if __name__ == '__main__':
    start()