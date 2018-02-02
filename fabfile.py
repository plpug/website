import os

from fabric.api import env, local, run

env.hosts = [os.environ['HOST']]
env.port = os.environ['PORT']


def script_config(name):
    if name == 'dev':
        env.user = os.environ['DEV_USER']
        env.cwd = os.environ['DEV_DIR']
    elif name == 'prod':
        env.user = os.environ['PRODUCTION_USER']
        env.cwd = os.environ['PRODUCTION_DIR']


def test():
    local("./manage.py test")


def check(name):
    script_config(name)
    run('git branch')
    run('whoami')
    run('python --version')
    run('which python')
    run('pwd')
    env.cwd = '{}/{}'.format(env.cwd, '')
    run('./manage.py')


def deploy(name):
    script_config(name)
    run('git fetch origin')
    run('git pull')
    run('pip install -r requirements.txt')
    env.cwd = '{}/{}'.format(env.cwd, '')
    run('./manage.py migrate')
    # run('./manage.py compilemessages')
    if name == 'prod':
        dir_name = 'uwsgi-website-master'
    else:
        dir_name = 'uwsgi-website-dev'
    run('sudo kill -3 `cat /tmp/{}.pid`'.format(dir_name))

