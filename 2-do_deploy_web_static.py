#!/usr/bin/python3
# Fabfile to distribute an archive to a web server.
# using the function do_deploy
# Prototype: def do_deploy(archive_path):
import os.path
from fabric.api import *

env.hosts = ["100.25.171.157", "34.229.56.239"]
env.user = "ubuntu"

def do_deploy(archive_path):
    """Distributes an archive to a web server.
    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        split_slash = archive_path.split("/")[-1]
        remove_tgz = split_slash.split(".")[0]
        directory = '/data/web_static/releases/'
        run('mkdir -p {}{}'.format(directory, remove_tgz))
        run('tar -xzf /tmp/{0}.tgz -C {1}{0}'.format(remove_tgz, directory))
        run('rm /tmp/{}.tgz'.format(remove_tgz))
        run('mv {0}{1}/web_static/* {0}{1}'.format(directory, remove_tgz))
        run('rm -rf {}{}/web_static'.format(directory, remove_tgz))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}\
                /data/web_static/current'.format(directory, remove_tgz))
        return True
    except Exception as e:
        return False
