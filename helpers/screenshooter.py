import os
from datetime import datetime


def get_screenshot(self):
    """
    Save screenshot to test-results/method_name folder
    """
    method_name = self._testMethodName
    class_name = type(self).__name__
    time_now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    folder = os.path.dirname(os.getcwd())
    directory = "".join([folder, "/test-results/", class_name])

    if not os.path.exists(directory):
        os.makedirs(directory)

    file_name = "%s/%s - %s.png" % (directory, time_now, method_name)

    self.driver.get_screenshot_as_file(file_name)
    # for jenkins integration
    print "[[ATTACHMENT|%s]]" % file_name
    print "current url - %s" % self.driver.current_url