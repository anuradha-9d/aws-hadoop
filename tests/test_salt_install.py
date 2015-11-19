import unittest
import sys
sys.path.append('../')
from ConfigParser import SafeConfigParser
from fabric_helper import *
import ast

class test_salt_install(unittest.TestCase):
    config = SafeConfigParser()
    host_user = None
    host_key_file = None

    def setUp(self):
        self.config.read('aws_hadoop.hosts')
        self.host_user = 'ubuntu'
        self.host_key_file = "~/.ssh/hadoopec2cluster.pem"


    def test_salt_ping(self):
        """Validates are all salt minions are responding to the ping"""
        main_config = SafeConfigParser()
        main_config.read('config.ini')
        saltmaster = eval(self.config.get("main", "saltmaster"))['ip_address']
        fb = fabric_helper(host_ip = saltmaster, host_user = self.host_user, host_key_file = self.host_key_file)
        salt_output = fb.run_salt_master_ping()
        hosts = ast.literal_eval(main_config.get('main','hadoop_nodes'))
        for host in hosts:
            self.assertTrue(eval(salt_output)[host])



