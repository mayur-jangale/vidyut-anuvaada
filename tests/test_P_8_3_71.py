# Test for प.8.3.71

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_8_3_71.py'
spec = importlib.util.spec_from_file_location('P_8_3_71', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P_8_3_71'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra8371


def test_P_8_3_71():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

