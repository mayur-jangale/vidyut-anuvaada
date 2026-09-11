# Test for प.1.1.32

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_1_1_32.py'
spec = importlib.util.spec_from_file_location('P_1_1_32', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P_1_1_32'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra1132


def test_P_1_1_32():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

