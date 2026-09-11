# Test for प.4.2.74

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_4_2_74.py'
spec = importlib.util.spec_from_file_location('P_4_2_74', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P_4_2_74'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra4274


def test_P_4_2_74():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

