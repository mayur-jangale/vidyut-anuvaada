# Test for प.7.3.20

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_7_3_20.py'
spec = importlib.util.spec_from_file_location('P_7_3_20', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P_7_3_20'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra7320


def test_P_7_3_20():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

