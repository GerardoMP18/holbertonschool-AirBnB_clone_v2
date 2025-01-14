#!/usr/bin/python3
""" Deploy archive! """


from fabric.operations import run, put
from fabric.api import env
import os
env.hosts = ['34.226.205.91', '54.163.37.58']


def do_deploy(archive_path):
    """ script (based on the file 1-pack_web_static.py) that distributes
    an archive to your web servers, using the function do_deploy:"""
    if os.path.exists(archive_path):
        archive = archive_path.split('/')[1]
        # [ versions, web_static_20170315003959.tgz]
        filename = archive.split('.')[0]
        # [web_static_20170315003959, tgz]
        path = '/data/web_static/releases/'
        # cargue el archivo en el directorio /tmp/
        put(archive_path, "/tmp/{}".format(archive))
        # descromprimir el archvio /data/web_static/releases/{filename}
        run('mkdir -p {}{}/'.format(path, filename))
        run('tar -xzf /tmp/{} -C {}{}/'.format(archive, path, filename))
        # Eliminar el archivo del servidor web
        run('rm /tmp/{}'.format(archive))
        # mover a la ruta path
        run('mv {}{}/web_static/* {}{}/'.format(path, filename,
                                                path, filename))
        run('rm -rf {}{}/web_static'.format(path, filename))
        # Elimine el enlace simbólico /data/web_static/current del servidor web
        run('rm -rf /data/web_static/current')
        # Crear un nuevo enlace simbólico
        run('ln -s {}{}/ /data/web_static/current'.format(path, filename))
        print('New version deployed!')
        return True
    else:
        return False
