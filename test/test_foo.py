from unittest import TestCase

from foo import foo


class FooTest(TestCase):

    def test_foo(self):
        doc = foo()
        self.assertRegex(doc, 'Widgets')
