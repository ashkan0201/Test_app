import sys 
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / 'src'))

from code import find
def test_find():
    assert find("code-bezan.ir","code") == True

def test_find1():
    assert find("ashkan-bezan.ir","ashkan") == True
