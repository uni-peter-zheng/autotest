from autotest.client import test


class error_initialize(test.test):
    version = 1

    def initialize(self):
        raise NameError("test a bug in initialize()")

    def execute(self):
        pass
