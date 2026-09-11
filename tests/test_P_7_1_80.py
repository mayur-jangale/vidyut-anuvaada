# Test for प.7.1.80

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_7_1_80.py'
spec = importlib.util.spec_from_file_location('P_7_1_80', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P_7_1_80'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra7180


def test_P_7_1_80():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

