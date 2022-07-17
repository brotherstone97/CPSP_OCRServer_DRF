#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""

    # runserver시 이미지 폴더 유무에 따라 폴더 생성
    if not os.path.isdir('media'):
        os.mkdir('media')
        os.mkdir('media/images')
        os.mkdir('media/images/temp')

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CPSP_DRF.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
