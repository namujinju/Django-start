# createsuperuser: 관리자 계정 생성
# runserver: 서버 구동

# migrate: 관리자 모드
# makemigrations: 데이터베이스 변경사항 찾기
# migrate: 데이터베이스 변경사항 반영
# shell: 장고 shell 모드


#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tempPjt.settings')
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
