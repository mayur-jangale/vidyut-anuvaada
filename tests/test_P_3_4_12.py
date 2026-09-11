# Test for प.3.4.12

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_3_4_12.py'
spec = importlib.util.spec_from_file_location('P_3_4_12', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P_3_4_12'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra3412


def test_P_3_4_12():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

