#!/usr/bin/python3
""" Compress before sending """


from fabric.operations import local
from datetime import datetime
from os.path import getsize


def do_pack():
    """  script that generates a .tgz archive from the contents of the
    web_static folder of your AirBnB Clone repo, using the function
    do_pack"""

    local("mkdir -p versions")
    date = datetime.utcnow()
    format_date = "%Y%m%d%H%M%S"
    conv = date.strftime(format_date)
    path = "versions/web_static_{}.tgz".format(conv)
    localhost = local("tar -cvzf {} web_static".format(path))

    if localhost.succeeded:
        print("web_static packed: {} -> {}Bytes".format(path, getsize(path)))
        return path
    elif localhost.failed:
        return None
