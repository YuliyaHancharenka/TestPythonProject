class Foo:
    def __init__(self, arg1, arg2):
        pass

def bar1(class_name):
    args = ("val1", "val2")
    local_class = class_name(*args)
    print('(Инициализация {0})'.format(local_class))

def bar2(class_name):
    kwargs = {'arg1':'val1','arg2':'val2'}
    local_class = class_name(**kwargs)
    print('(Инициализация {0})'.format(local_class))

one = bar1(Foo)
two = bar2(Foo)