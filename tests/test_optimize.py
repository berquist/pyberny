from importlib.resources import path

import pytest

from berny import Berny, geomlib, optimize
from berny.solvers import MopacSolver


@pytest.fixture
def mopac(scope='session'):
    return MopacSolver()


def ethanol():
    with path('tests', 'ethanol.xyz') as p:
        return geomlib.readfile(p), 5


def aniline():
    with path('tests', 'aniline.xyz') as p:
        return geomlib.readfile(p), 12


def cyanogen():
    with path('tests', 'cyanogen.xyz') as p:
        return geomlib.readfile(p), 4


def water():
    with path('tests', 'water.xyz') as p:
        return geomlib.readfile(p), 7


@pytest.mark.parametrize('test_case', [ethanol, aniline, cyanogen, water])
def test_optimize(mopac, test_case):
    geom, n_ref = test_case()
    berny = Berny(geom)
    optimize(berny, mopac)
    assert berny.converged
    assert berny._n == n_ref
