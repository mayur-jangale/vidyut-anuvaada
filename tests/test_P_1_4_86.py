# Test for प.1.4.86

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_1_4_86.py'
spec = importlib.util.spec_from_file_location('P_1_4_86', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P_1_4_86'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra1486


def test_P_1_4_86():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

