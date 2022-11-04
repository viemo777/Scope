import sys

print('any'.encode())

print(sys.path)
print(sys.api_version)
print(sys.getwindowsversion())
print(sys.int_info)
print(sys.platform)
print(sys.version_info)
print(sys.api_version)

pi = 'outer pi variable'


def print_pi():
    pi = 'inner pi variable'
    print(pi)


print_pi()
print(pi)

pi = 'global pi variable'


def inner():
    pi = 'inner pi variable'
    print(pi)


inner()
print(pi)

pi = 'global pi variable'


def outer():
    pi = 'outer pi variable'

    def inner():
        # pi = 'inner pi variable'
        nonlocal pi
        print(pi)

    inner()


outer()
print(pi)
