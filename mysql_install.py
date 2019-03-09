#!/usr/bin/python
#

import os
import sys
import socket

def getIp():
    return socket.gethostbyname(socket.gethostname()).split('.')[3]

def createFolder(mysql_full_path):
    print '''[note] create mysql dir %s''' % mysql_full_path
    os.makedirs(mysql_full_path)

def unTar(package_path,mysql_full_path):
    print '''[note] untar mysql package to %s''' % mysql_full_path
    os.system('tar -zxf %s -C %s' % (package_path,mysql_full_path))

def modifyConf(port,mysql_conf,mysql_full_path):
    for conf in mysql_conf:
        if port not in conf:
            print '''[note] port=%s -> %s''' % (port,conf)
            os.system('''sed -i 's/3301/%s/g' %s''' % (port,os.path.join(mysql_full_path,conf)))
        if 'my.cnf' in os.path.join(mysql_full_path,conf):
            print '''[note] server_id=%s%s -> %s''' % (getIp(),port,conf)
            os.system('''sed -i 's/11%s/%s%s/g' %s''' % (port,getIp(),port,os.path.join(mysql_full_path,conf)))

def main():
    package_path = '/root/db_version_v1.tar.gz'
    basepath = '/data/mysql/'
    mysql_conf = ['my.cnf','start.sh','login.sh']

    for port in sys.argv[1:]:
        mysql_full_path = os.path.join(basepath,str(port))
        if not os.path.exists(mysql_full_path):
            createFolder(mysql_full_path)
            unTar(package_path,mysql_full_path)
            modifyConf(port,mysql_conf,mysql_full_path)
            print '''[note] %s complete!!!\n''' % port

if __name__ == '__main__':
    main()
