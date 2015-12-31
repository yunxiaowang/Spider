import os
import time
import logging
from bs4 import BeautifulSoup as BS
import requests


LOG = logging.getLogger(__name__)

SAVE_SHELL = "automate-save-page-as/save_page_as"
SAVE_CMD = os.path.join(os.path.dirname(__file__), SAVE_SHELL)


class Spider(object):
    def __init__(self):
        self._setupLogging()

    def _setupLogging(self):
        console = logging.StreamHandler()
        log_format = "%(asctime)-15s %(levelname)s %(message)s"
        console.setFormatter(logging.Formatter(log_format))
        LOG.addHandler(console)
        LOG.setLevel(logging.DEBUG)

    def downloadFile(self, name, url):
        cmd = ''.join([SAVE_CMD, ' -b firefox --load-wait-time 6 --save-wait-time 7 -d ./save/', name, ' ', url])
        LOG.debug(cmd)
        os.system(cmd)


if __name__ == "__main__":
    spider = Spider()
    spider.downloadFile('222.html', 'http://ks.netease.com/blog?id=3472')
    # time.sleep(20)
