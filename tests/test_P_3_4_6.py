# Test for प.3.4.6

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_3_4_6.py'
spec = importlib.util.spec_from_file_location('P_3_4_6', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P_3_4_6'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra346


def test_P_3_4_6():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

