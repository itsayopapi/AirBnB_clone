#!/usr/bin/python3
from .engine.file_storage import FileStorage
from. import base_model


storage = FileStorage()
storage.reload()
