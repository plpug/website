import os

from fabric.api import env, local, run

env.hosts = [os.environ['PRODUCTION_HOST']]
env.port = os.environ['PRODUCTION_PORT']
env.user = os.environ['PRODUCTION_USER']


def test():
    local("./manage.py test")


def test_production():
    env.cwd = os.environ['PRODUCTION_DIR']
    run('git branch')


def deploy_production():
    env.cwd = os.environ['PRODUCTION_DIR']
    run('git fetch origin')
    run('git pull')


def deploy_dev():
    env.cwd = os.environ['DEV_DIR']
    run('git fetch origin')
    run('git pull')
