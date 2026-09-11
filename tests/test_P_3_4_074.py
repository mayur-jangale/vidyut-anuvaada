# Test for प74

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_3_4_074.py'
spec = importlib.util.spec_from_file_location('P74', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P74'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra3474


def test_P74():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

