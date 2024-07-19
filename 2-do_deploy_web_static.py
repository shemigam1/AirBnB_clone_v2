#!/usr/bin/python3

"""contains Fabric file to deploy web static"""

from fabric.api import local, run, put, env
from os.path import exists
env.hosts = ['100.24.74.22', '54.234.57.164']


def do_deploy(archive_path):
    """
    deploy compressed file to web server
    """
    try:
        if exists(archive_path):
            file_name_ext = archive_path.split("/")[-1]
            file_name = file_name_ext.split(".")[0]
            path = "/data/web_static/releases/"
            put(archive_path, "/tmp/")
            run('mkdir -p {}{}'.format(path, file_name))
            run('tar -xvzf /tmp/{} -C {}{}/'.format(file_name_ext, path, file_name))
            run('rm /tmp/{}'.format(file_name_ext))
            run('mv {0}{1}/web_static/* {0}{1}/'.format(path, file_name))
            run('rm -rf {}{}/web_static'.format(path, file_name))
            run('rm -rf /data/web_static/current')
            run('ln -s {}{}/ /data/web_static/current'.format(path, file_name))
            return True
        else:
            return False
    except:
        return False
