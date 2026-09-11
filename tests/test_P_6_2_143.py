# Test for प.6.2.143

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_6_2_143.py'
spec = importlib.util.spec_from_file_location('P_6_2_143', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P_6_2_143'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra62143


def test_P_6_2_143():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

