# Test for प41

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_3_4_041.py'
spec = importlib.util.spec_from_file_location('P41', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P41'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra3441


def test_P41():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

