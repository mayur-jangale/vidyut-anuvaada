# Test for प.3.1.82

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_3_1_82.py'
spec = importlib.util.spec_from_file_location('P_3_1_82', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P_3_1_82'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra3182


def test_P_3_1_82():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

