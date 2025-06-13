#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os # standard python module for operating system
import sys # standard python module for system-specific functionality

# The script is part of the standard Django project structure created during 
# project initialization.

def main():
    """Run administrative tasks."""

    # sets the default Django settings module to "mysite.settings"
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

    # Attempts to import Django's command-line tools
    try:
        from django.core.management import execute_from_command_line

    # If Django isn't found, it raises a error suggesting possible solutions
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Executes Django commands based on arguments provided to the script
    execute_from_command_line(sys.argv)

# script execution check: the main() function only runs when the file is
# executed directly
if __name__ == "__main__":
    main()
