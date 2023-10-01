import os
import sys

path = os.path.join(os.getcwd(), "src")

sys.path.append(path)

from for_testing import find

assert find("code-bezan.ir","code") == True
