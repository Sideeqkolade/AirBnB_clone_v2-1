#!/usr/bin/python3
# Fabfile to generates a .tgz archive from the contents of web_static.
# folder of your AirBnB Clone repo, using the function do_pack.
# Prototype: def do_pack():
# All files in the folder web_static must be added to the final archive
# All archives must be stored in the folder versions
# (your function should create this folder if it doesn’t exist
# The name of the archive created must be
# web_static_<year><month><day><hour><minute><second>.tgz
# The function do_pack must return the archive path if the
# archive has been correctly generated. Otherwise, it should return None
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
