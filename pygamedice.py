import random


class Die:
    def __init__(self, sides=2, value=0):
        if not sides >= 2:
            raise ValueError("Must set more than one side.")
        if not isinstance(sides, int):
            raise ValueError("Must set a whole number without decimals for number of sides.")
        self.value = value or random.randint(1, sides)

    def __int__(self):
        return self.value

    def __eq__(self, other):
        return int(self) == other

    def __ne__(self, other):
        return int(self) != other

    def __lt__(self, other):
        return int(self) < other

    def __gt__(self, other):
        return int(self) > other

    def __le__(self, other):
        return int(self) <= other

    def __ge__(self, other):
        return int(self) >= other

    def __add__(self, other):
        return int(self) + other

    def __radd__(self, other):
        return int(self) + other

    def __repr__(self):
        return str(self.value)



class D4(Die):
    def __init__(self):
        super().__init__(sides=4)

class D6(Die):
    def __init__(self):
        super().__init__(sides=6)

class D8(Die):
    def __init__(self):
        super().__init__(sides=8)

class D10(Die):
    def __init__(self):
        super().__init__(sides=10)

class D12(Die):
    def __init__(self):
        super().__init__(sides=12)

class D20(Die):
    def __init__(self):
        super().__init__(sides=20)