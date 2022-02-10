import main
from unittest import TestCase

class TestCamelCase(TestCase):

    def test_camelcase_sentence(self):

        self.assertEqual('helloWorld', main.camel_case('Hello World'))
        self.assertEqual('', main.camel_case(''))
        self.assertEqual('hello', main.camel_case('HEllO'))
        self.assertEqual('y0,Wh84M3!!', main.camel_case('Y0, WH8 4 M3!!'))
        self.assertEqual('helloWorld', main.camel_case('  HELLO             WORLD'))