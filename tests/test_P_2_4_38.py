# Test for प.2.4.38

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_2_4_38.py'
spec = importlib.util.spec_from_file_location('P_2_4_38', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P_2_4_38'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra2438


def test_P_2_4_38():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

