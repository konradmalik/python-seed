import pytest
from example.demo import demo

@pytest.fixture(autouse=True)
def run_around_tests():
    # Code that will run before your test, for example:
    print("Preparing for test")
    # A test function will be run at this point
    yield
    # Code that will run after your test, for example:
    __clean()

def __clean():
    print("cleaning")

def demo_test():
    v = demo.get_value()
    assert v == 'demo'
