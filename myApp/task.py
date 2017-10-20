from celery import task
import time


@task
def celery_demo():
    """让耗时操作成为一个任务"""
    print("myapp is a good app.")
    time.sleep(5)
    print("myapp is a nice app.")