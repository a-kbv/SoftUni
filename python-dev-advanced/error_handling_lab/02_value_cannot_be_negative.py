class ValueCannotBeNegative(Exception):
    def __init__(self, value):
        self.value = value
        msg = f"Value {value} is negative"
        super(ValueCannotBeNegative, self).__init__(msg)

n = 5
for _ in range(5):
    x = int(input())
    if x < 0:
        raise ValueCannotBeNegative(x)

