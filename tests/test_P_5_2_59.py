# Test for प.5.2.59

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_5_2_59.py'
spec = importlib.util.spec_from_file_location('P_5_2_59', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P_5_2_59'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra5259


def test_P_5_2_59():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

