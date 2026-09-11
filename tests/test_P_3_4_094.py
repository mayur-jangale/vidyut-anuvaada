# Test for प94

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_3_4_094.py'
spec = importlib.util.spec_from_file_location('P94', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P94'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra3494


def test_P94():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

