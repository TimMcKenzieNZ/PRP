#!/usr/bin/env python
import os
import sys
from dotenv import load_dotenv
from os.path import join, dirname

# loads the given database configuration vairables from the .environ file into the server PATH environment
dotenv_path = join(dirname(__file__), '..', '.env')
if os.path.isfile(dotenv_path):
    load_dotenv(dotenv_path)

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prp.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
