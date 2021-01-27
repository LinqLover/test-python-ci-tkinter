from unittest import TestCase

import sys; print(sys.version_info)
from foo import foo


class FooTest(TestCase):

    def test_foo(self):
        doc = foo()
        self.assertRegex(doc, 'Widgets')
