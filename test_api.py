import warnings

import radvel
import radvel.driver
import numpy as np
import radvel.prior

warnings.filterwarnings("ignore")
warnings.simplefilter('once', DeprecationWarning)


class _args(object):
    def __init__(self):
        self.outputdir = '/tmp/'
        self.decorr = False

        self.nwalkers = 50
        self.nsteps = 100
        self.ensembles = 8


def test_k2131(setupfn='example_planets/k2-131.py'):
    """
    Check GP fit
    """
    args = _args()
    args.setupfn = setupfn

    radvel.driver.fit(args)
    
#    args.type = ['rv']
#    args.plotkw = {}
#    radvel.driver.plots(args)
    
import timeit 

print(timeit.timeit(test_k2131,number=1))
