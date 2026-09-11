# Test for प.6.4.63

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_6_4_63.py'
spec = importlib.util.spec_from_file_location('P_6_4_63', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P_6_4_63'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra6463


def test_P_6_4_63():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

