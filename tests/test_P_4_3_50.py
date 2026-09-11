# Test for प.4.3.50

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_4_3_50.py'
spec = importlib.util.spec_from_file_location('P_4_3_50', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P_4_3_50'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra4350


def test_P_4_3_50():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

