#!/usr/bin/python3
""" construct models directory """
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
