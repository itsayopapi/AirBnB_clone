#!/usr/bin/python3

"""
python initialisation file for packages.
Here we import all modules that are neccessary for our project
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
