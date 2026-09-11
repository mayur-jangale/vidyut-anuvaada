# Test for प111

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_3_4_111.py'
spec = importlib.util.spec_from_file_location('P111', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P111'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra34111


def test_P111():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

