#!/usr/bin/python3

"""contains Fabric file to deploy web static"""

from datetime import datetime
from fabric.api import local, run, put, env
from os.path import exists
env.hosts = ['100.24.74.22', '54.234.57.164']


def do_pack():
    """
    compress web static
    """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir('versions') is False:
            local('mkdir versions')
        file_name = 'versions/web_static_{}.tgz'.format(date)
        local('tar -cvzf {} web_static'.format(file_name))
        return file_name
    except:
        return None

def do_deploy(archive_path):
    """
    deploy compressed file to web server
    """
    if exists(archive_path):
        fn_ext = archive_path.split("/")[-1]
        fname = fn_ext.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run('sudo mkdir -p {}{}'.format(path, fname))
        run('sudo tar -xvzf /tmp/{} -C {}{}/'.format(fn_ext, path, fname))
        run('sudo rm /tmp/{}'.format(fn_ext))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, fname))
        run('rm -rf {}{}/web_static'.format(path, fname))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, fname))
        return True
    else:
        return False

def deploy():
    """deploy deploy deploy!"""
    archive = do_pack()
    if archive:
        return do_deploy(archive)
    else:
        return False
