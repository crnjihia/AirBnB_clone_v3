#!/usr/bin/python3
"""
Fabric script to generate a .tgz archive from the web_static folder,
saving it in a 'versions' directory with a timestamped filename.
"""

from fabric.api import *
from datetime import datetime


def do_pack():
    """
    Creates a .tgz archive of web_static in 'versions' directory.
    Returns the archive path if successful, otherwise None.
    """
    local("sudo mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(date)
    result = local("sudo tar -cvzf {} web_static".format(filename))
    if result.succeeded:
        return filename
    else:
        return None
