# Test for प.6.1.60

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_6_1_60.py'
spec = importlib.util.spec_from_file_location('P_6_1_60', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P_6_1_60'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra6160


def test_P_6_1_60():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

