#!/usr/bin/python3
"""
    Fabric script that distributes an archive to the web servers.
"""
from os import path
from fabric.api import env, put, run

env.hosts = ['35.229.40.200', '35.229.23.118']


def do_deploy(archive_path):
    """ Function that distributes the archive.

    Args:
        archive_path (str): the path of the archive to deploy on the servers.
    """

    try:
        if not path.exists(archive_path):
            raise FileNotFoundError

        name = archive_path.split("/")[-1]
        name_no_ext = name.split(".")[0]

        remote = "/data/web_static/releases"
        dest = "{}/{}".format(remote, name_no_ext)

        put(archive_path, '/tmp')
        run('mkdir -p {}/'.format(dest))
        run('tar -xzf /tmp/{} -C {}'.format(name, dest))
        run('rm /tmp/{}'.format(name))
        run('mv {}/web_static/* {}/'.format(dest, dest))
        run('rm -rf {}/web_static'.format(dest))
        run('rm -rf /data/web_static/current')
        run('ln -s {}/ /data/web_static/current'.format(dest))

    except:
        print("Error. Version deploy aborted")
        return False

    print("New version deployed!")
    return True
