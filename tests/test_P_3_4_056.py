# Test for प56

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_3_4_056.py'
spec = importlib.util.spec_from_file_location('P56', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P56'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra3456


def test_P56():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

