import subprocess
import threading


def django():
    cmd = ["python", "justship/manage.py", "runserver", "0.0.0.0:8000"]
    subprocess.run(cmd)

def create_super_user():
    cmd = ["python", "justship/manage.py", "createsuperuser"]
    subprocess.run(cmd)

def celery():
    cmd = ["/bin/zsh", "celery.sh"]
    subprocess.run(cmd)



def server():
    t1 = threading.Thread(target=celery)
    t2 = threading.Thread(target=django)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
