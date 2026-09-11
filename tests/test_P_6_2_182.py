# Test for प.6.2.182

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_6_2_182.py'
spec = importlib.util.spec_from_file_location('P_6_2_182', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P_6_2_182'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra62182


def test_P_6_2_182():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

