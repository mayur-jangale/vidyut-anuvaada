# Test for प.6.4.59

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_6_4_59.py'
spec = importlib.util.spec_from_file_location('P_6_4_59', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P_6_4_59'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra6459


def test_P_6_4_59():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

