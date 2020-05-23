"""
A module for defining the config parameters globally
"""

import os
import string

current_abs_path = os.path.split(os.path.realpath(__file__))[0]
#print(current_abs_path)

configs = {}

configs["run_name_choices"] = ["c", "a", "A", "C"]
configs["valid_proj_type"] = ["ml", "dl", "ML", "DL"]

configs["data_loader_types"] = ["img", "text", "csv", "IMG", "TEXT", "CSV"]
configs["nn_architecture_types"] = ["cnn", "lstm", "nn", "CNN", "LSTM", "NN"]

configs["proj_name_first_char"] = string.ascii_lowercase
configs["proj_name_allowed_char"] = string.ascii_lowercase + string.digits + "_" + "-"
configs["proj_name_length"] = 80


configs["ml_template_path"] = os.path.join(current_abs_path, "data/ml")
configs["dl_template_path"] = os.path.join(current_abs_path, "data/dl")
configs["data_loader_path"] = os.path.join(current_abs_path, "data/loader")
configs["network_template_path"] = os.path.join(current_abs_path, "data/network")


if __name__ == "__main__":
    print(configs["proj_name_first_char"])
    print(configs["proj_name_allowed_char"])