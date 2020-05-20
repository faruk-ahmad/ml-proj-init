"""
the main module of ml-proj-init library
"""

import os
import sys
import argparse

# import required classes
from .utils import Utility
from .validation import Validation
from .config import configs

# lets create obj of Utility and Validation class
util = Utility()
val = Validation()


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
                                metavar="mode",
                                type=str,
                                choices=configs["run_name_choices"],
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
                                metavar="name",
                                type=str,
                                help="Project name to initialize the project.",
                                required=False
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
                                metavar="path",
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
                                metavar="type",
                                type=str,
                                help="Type of project to create project structure.",
                                choices=configs["valid_proj_type"],
                                default="ml",
                                required=False
                                )

    """
    User can pass the type of data loader to add to the project with this argument.
    """
    ml_proj_parser.add_argument(
                                "-l",
                                "--loader",
                                metavar="loader",
                                help="Type of data loader to add to project",
                                choices=configs["data_loader_types"],
                                required=False
                                )

    """
    User can pass the type of network architecture to add to the project with this argument.
    """
    ml_proj_parser.add_argument(
                                "-net",
                                "--network",
                                metavar="network",
                                help="Type of network architecture to add to the project",
                                choices=configs["nn_architecture_types"],
                                required=False
                                )

    ml_proj_args = ml_proj_parser.parse_args()
    
    proj_mode = ml_proj_args.mode.lower()
    proj_path = ml_proj_args.path
    proj_name = ml_proj_args.name
    proj_type = ml_proj_args.type.lower()

    data_loader_type = ml_proj_args.loader
    network_architecture_type = ml_proj_args.network

    print(f'Proj Mode: {proj_mode}\nProj Path: {proj_path}\nProj Name: {proj_name}\nProj Type: {proj_type}\nData Loader: {data_loader_type}\nNetwork Architecture: {network_architecture_type}')

    # now lets validate all the arguments and take decision what to do next with those arguments
    GOOD_TO_GO_CREATE = False
    GOOD_TO_GO_APPEND = False


    # if the project path is not given, we assume current working directory as the path.
    if proj_path is None:
        proj_path = os.getcwd()
    print(f"Project Path: {proj_path}")

    # lets start with the creation mode

    if proj_mode == "c":
        #check if the path is valid
        if val.is_valid_path(proj_path):
            if val.is_valid_project_name(proj_name):
                proj_dir = os.path.join(proj_path, proj_name)
                if val.is_path_exists(proj_dir):
                    consent = util.get_user_consent()
                    if consent == "y":
                        print(f"Deleting existing directory: {proj_dir}...")
                        deleted = util.delete_existing_path(proj_dir)
                    else:
                        print(f"Exiting...")
                        sys.exit(0)
                created = util.create_project_structure(proj_type, proj_dir)
                if created:
                    print("Project structure created.")
                else:
                    print("Something went wrong, check the arguments.")
            else:
                print(f"{proj_name} is invalid.")
                sys.exit(0)
        else:
            print(f"{proj_path} is invalid.")
            sys.exit(0)


    # lets work on the append mode now

    if proj_mode.lower() == "a":
        # check if all the argument for append mode are None, then exit
        if data_loader_type is None and network_architecture_type is None:
            print(f"Nothing to append. Exiting...")
            sys.exit(0)

        # lets check if there is anything to do with data loader
        if data_loader_type is not None:
            data_loader = data_loader_type.lower()
            if val.is_valid_path(proj_path):
                data_loader_appended = util.append_data_loader(proj_path, data_loader)
                if data_loader_appended:
                    print(f"{data_loader} - data loader added to project. Check {proj_path}/src directory.")
                else:
                    print(f"Something went wrong with appending data loader.")
                    sys.exit(0)


        # lets check if there is anything to do with network architecture
        if network_architecture_type is not None:
            network_type = network_architecture_type.lower()
            if val.is_valid_path(proj_path):
                network_type_appended = util.append_network_architecture(proj_path, network_type)
                if network_type_appended:
                    print(f"{network_type} - network architecture added to project. Check {proj_path}/src directory.")
                else:
                    print(f"Something went wrong with appending network architecture.")
                    sys.exit(0)



if __name__ == '__main__':
    start()