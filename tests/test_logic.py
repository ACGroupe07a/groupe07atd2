from unittest import TestCase
import logic

class LogicTests(TestCase):

        def test_and(self):
                self.assertEquals(operators.and_(True, True),False)

        def test_or(self):
                self.assertEquals(operators.or_(True,False),True)
