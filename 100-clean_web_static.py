#!/usr/bin/python3
"""
Fabric script to clean out-of-date web static archives.

Deletes unnecessary archives in local and remote servers.
Usage: fab -f 100-clean_web_static.py do_clean:number=n
"""
from fabric.api import local, run, env
import os

env.hosts = ['54.158.183.40', '35.174.205.229']


def do_clean(number=0):
    """
    Delete out-of-date archives in local and remote servers.

    Args:
        number (int): Number of recent archives to keep.
                      Default is 0 (keep only most recent).
    """
    # Ensure number is at least 1
    number = max(int(number), 1)

    # Clean local versions directory
    local_archives = sorted(local('ls versions', capture=True).split())
    to_delete_local = local_archives[:-number]
    for archive in to_delete_local:
        local(f'rm versions/{archive}')

    # Clean remote releases directory on both servers
    run_func = run  # Use run for remote commands
    remote_archives = sorted(run('ls /data/web_static/releases').split())
    to_delete_remote = remote_archives[:-number]
    for archive in to_delete_remote:
        if archive.startswith('web_static_'):
            run(f'rm -rf /data/web_static/releases/{archive}')
