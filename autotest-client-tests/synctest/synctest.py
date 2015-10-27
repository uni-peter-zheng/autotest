import os

from autotest.client import test
from autotest.client.shared import utils


class synctest(test.test):
    version = 1
    preserve_srcdir = True

    def initialize(self):
        self.job.require_gcc()

    def setup(self):
        os.chdir(self.srcdir)
        utils.make()

    def run_once(self, len, loop, testdir=None):
        args = len + ' ' + loop
        output = os.path.join(self.srcdir, 'synctest ')
        if testdir:
            os.chdir(testdir)
        utils.system(output + args)
