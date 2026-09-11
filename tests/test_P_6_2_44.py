# Test for प.6.2.44

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_6_2_44.py'
spec = importlib.util.spec_from_file_location('P_6_2_44', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P_6_2_44'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra6244


def test_P_6_2_44():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

