from flask_frozen import Freezer
from jmcnally import jmcnally

freezer = Freezer(jmcnally)

if __name__ == '__main__':
    freezer.freeze()
