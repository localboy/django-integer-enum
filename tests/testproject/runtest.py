import os, sys

import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.testproject.settings'

test_dir = os.path.dirname(__file__)
sys.path.insert(0, test_dir)

django.setup()

from django.test.utils import get_runner
from django.conf import settings

def runtests():
    app_label = ['testapp']
    if django.VERSION < (1, 8):
        from django.test.simple import DjangoTestSuiteRunner
        def run_tests(app_label, verbosity, interactive):
            runner = DjangoTestSuiteRunner(verbosity=verbosity, interactive=interactive, failfast=False)
            return runner.run_tests(app_label)
    else:
        from django.test.runner import DiscoverRunner
        def run_tests(app_label, verbosity, interactive):
            runner = DiscoverRunner(verbosity=verbosity, interactive=interactive, failfast=False)
            return runner.run_tests(app_label)
    failures = run_tests(app_label, verbosity=1, interactive=True)
    sys.exit(failures)

if __name__ == '__main__':
    runtests()