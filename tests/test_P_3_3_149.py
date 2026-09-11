# Test for प.3.3.149

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_3_3_149.py'
spec = importlib.util.spec_from_file_location('P_3_3_149', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P_3_3_149'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra33149


def test_P_3_3_149():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

