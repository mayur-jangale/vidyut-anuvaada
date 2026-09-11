# Test for प36

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_3_4_036.py'
spec = importlib.util.spec_from_file_location('P36', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P36'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra3436


def test_P36():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

