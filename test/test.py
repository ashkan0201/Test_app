import os
import sys

path = os.path.join(os.getcwd(), "src")

sys.path.append(path)

from for_testing import find
def test_find():
    assert find("code-bezan.ir","code") == True

def test_find1():
    assert find("ashkan-bezan.ir","ashkan") == True
