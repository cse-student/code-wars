def truthy():
    print("True")

def falsey():
    print("False")


def _if(boolean, func1, func2):
    if (boolean):
        return func1()
    else:
        return func2()

_if(True, truthy, falsey)
_if(False, truthy, falsey)
