"""
A module for defining the config parameters globally
"""

import os
import string

current_abs_path = os.path.abspath(os.path.dirname(__file__))
print(current_abs_path)

config = {
    "run_name_choices": ["c", "a"],
    "proj_name_first_char": string.ascii_lowercase,
    "proj_name_allowed_char": string.ascii_lowercase + string.digits + "_" + "-",
    "proj_name_length": 80,
    "valid_proj_type": ["ml", "dl"],
    "ml_template_path": os.path.join(current_abs_path, "data/ml"),
    "dl_template_path": os.path.join(current_abs_path, "data/dl")
}


if __name__ == "__main__":
    print(config["proj_name_first_char"])
    print(config["proj_name_allowed_char"])