# Test for प.7.4.47

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_7_4_47.py'
spec = importlib.util.spec_from_file_location('P_7_4_47', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P_7_4_47'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra7447


def test_P_7_4_47():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

