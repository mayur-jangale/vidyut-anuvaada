# Test for प.5.4.16

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_5_4_16.py'
spec = importlib.util.spec_from_file_location('P_5_4_16', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P_5_4_16'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra5416


def test_P_5_4_16():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

