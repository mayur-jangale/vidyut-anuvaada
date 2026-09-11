# Test for प.2.3.50

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_2_3_50.py'
spec = importlib.util.spec_from_file_location('P_2_3_50', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P_2_3_50'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra2350


def test_P_2_3_50():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

