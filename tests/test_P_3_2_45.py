# Test for प.3.2.45

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_3_2_45.py'
spec = importlib.util.spec_from_file_location('P_3_2_45', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P_3_2_45'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra3245


def test_P_3_2_45():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

