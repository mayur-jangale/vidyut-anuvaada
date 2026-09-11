# Test for प.1.1.15

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_1_1_15.py'
spec = importlib.util.spec_from_file_location('P_1_1_15', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P_1_1_15'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra1115


def test_P_1_1_15():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

