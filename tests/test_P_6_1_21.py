# Test for प.6.1.21

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_6_1_21.py'
spec = importlib.util.spec_from_file_location('P_6_1_21', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P_6_1_21'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra6121


def test_P_6_1_21():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

