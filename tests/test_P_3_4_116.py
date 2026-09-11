# Test for प116

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_3_4_116.py'
spec = importlib.util.spec_from_file_location('P116', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P116'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra34116


def test_P116():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

