# Test for P_1_3_75

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_1_3_75.py'
spec = importlib.util.spec_from_file_location('P_1_3_75', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P_1_3_75'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra1375


def test_P_1_3_75():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

