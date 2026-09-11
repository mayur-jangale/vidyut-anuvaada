# Test for प.6.2.153

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_6_2_153.py'
spec = importlib.util.spec_from_file_location('P_6_2_153', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P_6_2_153'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra62153


def test_P_6_2_153():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

