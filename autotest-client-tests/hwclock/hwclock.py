import re
import logging

from autotest.client import test, utils
from autotest.client.shared import error


class hwclock(test.test):
    version = 1

    def run_once(self):
        """
        Set hwclock back to a date in 1980 and verify if the changes took
        effect in the system.
        """
        logging.info('Setting hwclock to 2/2/80 03:04:00')
        utils.system('/sbin/hwclock --set --date "2/2/80 03:04:00"')
        date = utils.system_output('LC_ALL=C /sbin/hwclock')
        if not re.match('Sat *Feb *2 *03:04:.. 1980', date):
            raise error.TestFail("Failed to set hwclock back to the eighties. "
                                 "Output of hwclock is '%s'" % date)

    def cleanup(self):
        """
        Restore hardware clock to current system time.
        """
        logging.info('Restoring the hardware clock')
        utils.system('/sbin/hwclock --systohc --noadjfile --utc')
