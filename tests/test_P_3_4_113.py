# Test for प113

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_3_4_113.py'
spec = importlib.util.spec_from_file_location('P113', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P113'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra34113


def test_P113():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

