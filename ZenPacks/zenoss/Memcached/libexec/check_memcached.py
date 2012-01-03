#!/usr/bin/env python
###########################################################################
#
# This program is part of Zenoss Core, an open source monitoring platform.
# Copyright (C) 2008, Zenoss Inc.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 or (at your
# option) any later version as published by the Free Software Foundation.
#
# For complete information please visit: http://www.zenoss.com/oss/
#
###########################################################################

import sys
import types
import socket
from optparse import OptionParser


class ZenossMemcachedStatsPlugin:
    def __init__(self, host, port=11211):
        self.host = host
        self.port = port
        self.buffer = ""

    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        try:
            s.connect((self.host, int(self.port)))
        except socket.timeout:
            print "Connecton timed out."
            sys.exit(1)
        except socket.error, msg:
            if type(msg) is types.TupleType:
                msg = msg[1]

            print "Connection error: %s" % (msg[1],)
            sys.exit(1)

        dps = []

        s.sendall("stats\n")
        while 1:
            line = self.readline(s)
            if not line or line.strip() == 'END':
                break

            garbage, dp, value = line.split(' ', 2)
            dps.append((dp, value))

        if s:
            s.close()

        print "memcached stats|%s" % (' '.join(map('='.join, dps)),)
        sys.exit(0)

    def readline(self, socket):
        buf = self.buffer
        recv = socket.recv
        while True:
            index = buf.find('\r\n')
            if index >= 0:
                break
            data = recv(4096)
            if not data:
                print "Connection closed prematurely"
                sys.exit(1)
            buf += data
        if index >= 0:
            self.buffer = buf[index + 2:]
            buf = buf[:index]
        else:
            self.buffer = ''
        return buf


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option('-H', '--host', dest='host',
        help='Hostname of memcached server')
    parser.add_option('-p', '--port', dest='port', default='11211',
        help='Port that memcached is listening on')
    options, args = parser.parse_args()

    if not options.host:
        print "You must specify the host parameter."
        sys.exit(1)

    cmd = ZenossMemcachedStatsPlugin(options.host, options.port)
    cmd.run()
