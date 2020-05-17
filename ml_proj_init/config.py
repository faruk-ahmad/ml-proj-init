"""
A module for defining the config parameters globally
"""

import os
import string

config = {
    "run_name_choices": ["c", "a"],
    "proj_name_first_char": string.ascii_lowercase,
    "proj_name_allowed_char": string.ascii_lowercase + string.digits + "_",
    "proj_name_length": 80
}