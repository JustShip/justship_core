import subprocess
import threading
import shlex


def django():
    cmd = "python justship/manage.py runserver 0.0.0.0:8000"
    __run_command(cmd)


def create_super_user():
    cmd = "python justship/manage.py createsuperuser"
    __run_command(cmd)


def celery():
    cmd = "/bin/sh celery.sh"
    __run_command(cmd)


def test() -> None:
    """
    Run django tests
    :return: None
    """
    cmd = "python justship/manage.py test"
    __run_command(cmd)


def __run_command(command: str) -> str:
    """
    Run a command process
    :param command: a string that represent the command to execute
    :return: string with de stdout
    """
    parsed_command = shlex.split(command)
    process = subprocess.run(parsed_command, stdout=subprocess.PIPE, universal_newlines=True)
    return process.stdout


def server():
    t1 = threading.Thread(target=celery)
    t2 = threading.Thread(target=django)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
