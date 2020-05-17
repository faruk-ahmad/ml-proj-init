"""
the main module of ml-proj-init library
"""

import os
import sys
import argparse



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
    ml_proj_parser.add_argument(
                                "-n",
                                "--name",
                                type=str,
                                help="Project name to initialize the project.",
                                required=True
                                )

    ml_proj_parser.add_argument(
                                "-p",
                                "--path",
                                type=str,
                                help="A valid path to create the project stucture.",
                                required=False
                                )

    ml_proj_args = ml_proj_parser.parse_args()
    print(ml_proj_args)


if __name__ == '__main__':
    start()