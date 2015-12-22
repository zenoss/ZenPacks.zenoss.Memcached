##############################################################################
#
# Copyright (C) Zenoss, Inc. 2015, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################

from Products.ZenTestCase.BaseTestCase import BaseTestCase
from ZenPacks.zenoss.Memcached.libexec.check_memcached import\
    (ZenossMemcachedStatsPlugin,)
from mock import Mock


RESULT = 'STAT pid 1943\r\nSTAT uptime 28220\r\nSTAT time 1450719287\r\nSTAT \
version 1.4.4\r\nSTAT pointer_size 64\r\nSTAT rusage_user 2.081683\r\nSTAT \
rusage_system 2.577608\r\nSTAT curr_connections 31\r\nSTAT total_connections \
192\r\nSTAT connection_structures 44\r\nSTAT cmd_get 125935\r\nSTAT cmd_set \
66618\r\nSTAT cmd_flush 0\r\nSTAT get_hits 95784\r\nSTAT get_misses \
30151\r\nSTAT delete_misses 0\r\nSTAT delete_hits 0\r\nSTAT incr_misses \
1\r\nSTAT incr_hits 59\r\nSTAT decr_misses 0\r\nSTAT decr_hits 0\r\nSTAT \
cas_misses 0\r\nSTAT cas_hits 0\r\nSTAT cas_badval 0\r\nSTAT auth_cmds \
0\r\nSTAT auth_errors 0\r\nSTAT bytes_read 45093185\r\nSTAT bytes_written \
37030894\r\nSTAT limit_maxbytes 67108864\r\nSTAT accepting_conns 1\r\nSTAT \
listen_disabled_num 0\r\nSTAT threads 4\r\nSTAT conn_yields 1460\r\nSTAT bytes \
43957676\r\nSTAT curr_items 62974\r\nSTAT total_items 66618\r\nSTAT evictions \
0\r\nEND\r\n'


class TestPack(BaseTestCase):
    """
    Tests for objects loaded from ZP.
    Checks for templates and graph definitions.
    """

    def afterSetUp(self):
        super(TestPack, self).afterSetUp()
        self.socket = Mock()
        self.socket.recv.return_value = RESULT

    def testRun(self):
        self.assertIn('run', dir(ZenossMemcachedStatsPlugin))
        self.assertTrue(callable(ZenossMemcachedStatsPlugin.run))

    def testReadLine(self):
        plugin = ZenossMemcachedStatsPlugin('0.0.0.0')
        res = plugin.readline(self.socket)
        self.assertEqual(res, 'STAT pid 1943')
        self.assertTrue(len(plugin.buffer) > 0)


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestPack))
    return suite
