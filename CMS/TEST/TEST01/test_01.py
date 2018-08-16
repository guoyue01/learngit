# content of test_module.py
import pytest


@pytest.fixture(scope="module", params=["mod1", "mod2"])
def modarg(request):
    param = request.param
    print("  SETUP modarg %s" % param)
    yield param
    print("  TEARDOWN modarg %s" % param)


@pytest.fixture(scope="function", params=[{"a":1,"b":1}, {"a":1,"b":2}])
def otherarg(request):
    param = request.param
    print("  SETUP otherarg %s" % param)
    yield param
    print("  TEARDOWN otherarg %s" % param)


def test_0(modarg):
    print("  RUN test0 with otherarg %s" % modarg['a'])


def test_1(modarg):
    print("  RUN test1 with modarg %s" % modarg)


def test_2(otherarg, modarg):
    print("  RUN test2 with otherarg %s and modarg %s" % (otherarg, modarg))


