# HUMAN, STUDENT, controller

from model import *


class God:
    @staticmethod
    def test(human):
        if isinstance(human, Human):
            human.run()


h = Human("Alex", " M.", 20)
s = Student("Alex", " M.", 20)

God.test(h)
God.test(s)
