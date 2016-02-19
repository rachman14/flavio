import unittest
import numpy as np
from . import rge
from . import common
from . import wilsoncoefficients
from .. import eft
from ..running import running

s = 1.519267515435317e+24

par = {
    'm_e': 0.510998928e-3,
    'm_mu': 105.6583715e-3,
    'm_tau': 1.77686,
    'm_B+': 5.27929,
    'm_B0': 5.27961,
    'm_Bs': 5.36679,
    'm_K*0': 0.89166,
    'tau_B+': 1638.e-15*s,
    'tau_B0': 152.e-14*s,
    'alpha_e': 1/127.940,
    'alpha_s': 0.1185,
    'm_Z': 91.1876,
    'm_b': 4.17,
    'm_t': 173.1,
    'm_c': 1.275,
    'GF': 1.1663787e-5,
    'Vus': 0.22,
    'Vub': 3.7e-3,
    'Vcb': 4.1e-2,
    'gamma': 1.22,
}

class TestBWilson(unittest.TestCase):
    def test_running(self):
        c_in = np.array([ 0.85143759,  0.31944853,  0.30029457,  0.82914154,  0.11154786,
        0.80629828,  0.32082766,  0.1300508 ,  0.69393572,  0.98427495,
        0.76415058,  0.90545245,  0.03290275,  0.89359186,  0.46273251])
        c_out = rge.run_wc_df1(par, c_in, 173.1, 4.2)

    def test_wctot(self):
        wc_low_correct = np.array([ -2.93671059e-01,   1.01676402e+00,  -5.87762813e-03,
        -8.70666812e-02,   4.11098919e-04,   1.10641294e-03,
        -2.95667920e-01,  -1.63048361e-01,   4.11363023e+00,
        -4.19345312e+00,   3.43507549e-03,   1.22202095e-03,
        -1.03192325e-03,  -1.00703396e-04,  -3.17810374e-03])
        wc_low_correct = np.concatenate([wc_low_correct, np.zeros(19)])
        wc_obj = eft.WilsonCoefficients()
        wc_low = wilsoncoefficients.wctot_dict(wc_obj, 'bsmumu', 4.2, par)
        wc_low_array = np.asarray([wc_low[key] for key in wc_obj.coefficients['bsmumu']])
        np.testing.assert_almost_equal(wc_low_array, wc_low_correct, decimal=8)
