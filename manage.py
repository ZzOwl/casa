#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inproj.settings')
    try:
        from django.core.management import execute_from_command_line
        sure_input = int(input("Type your id here :"))
        print("your id {0} confirmed.".format(sure_input))
    except ImportError as exc :
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    except ValueError as e :
        raise ImportError(
            "Just integer type is acceptable. Are you sure you enter your number !"
            "juster enter your number id"
        ) from e
    execute_from_command_line(sys.argv)  


if __name__ == '__main__':
    main()
