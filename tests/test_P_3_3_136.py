# Test for प.3.3.136

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_3_3_136.py'
spec = importlib.util.spec_from_file_location('P_3_3_136', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P_3_3_136'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra33136


def test_P_3_3_136():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

