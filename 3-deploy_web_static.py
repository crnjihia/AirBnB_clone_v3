#!/usr/bin/python3
"""
Fabric script for automated web static deployment.

This script provides functionality to:
1. Create a compressed archive of web_static directory
2. Deploy the archive to remote web servers
3. Set up the deployment on remote servers

Requirements:
- Fabric library
- SSH access to remote servers
- Web servers configured to receive static content

Usage:
fab -f 3-deploy_web_static.py deploy -i ~/.ssh/id_rsa -u ubuntu
"""
from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir


env.hosts = ['54.158.183.40', '35.174.205.229']


def do_pack():
    """
    Generates a compressed archive from the web_static folder.

    Creates a timestamped .tgz archive in the 'versions' directory.

    Returns:
        str: Path to the created archive, or None if creation fails
    """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")

        if not isdir("versions"):
            local("mkdir versions")

        file_name = f"versions/web_static_{date}.tgz"

        local(f"tar -cvzf {file_name} web_static")

        return file_name
    except Exception as e:
        print(f"Error creating archive: {e}")
        return None


def do_deploy(archive_path):
    """
    Distributes and deploys an archive to web servers.

    Args:
        archive_path (str): Path to the archive to be deployed

    Returns:
        bool: True if deployment succeeds, False otherwise
    """
    # Verify archive exists before attempting deployment
    if not exists(archive_path):
        return False

    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        release_path = "/data/web_static/releases/"

        put(archive_path, '/tmp/')

        run(f'mkdir -p {release_path}{no_ext}/')

        run(f'tar -xzf /tmp/{file_n} -C {release_path}{no_ext}/')

        run(f'rm /tmp/{file_n}')

        run(f'mv {release_path}{no_ext}/web_static/* {release_path}{no_ext}/')

        run(f'rm -rf {release_path}{no_ext}/web_static')

        run('rm -rf /data/web_static/current')
        run(f'ln -s {release_path}{no_ext}/ /data/web_static/current')

        return True
    except Exception as e:
        print(f"Error during deployment: {e}")
        return False


def deploy():
    """
    Orchestrates the entire deployment process.

    Creates an archive and deploys it to web servers.

    Returns:
        bool: True if full deployment succeeds, False otherwise
    """
    archive_path = do_pack()

    if archive_path is None:
        return False

    return do_deploy(archive_path)
