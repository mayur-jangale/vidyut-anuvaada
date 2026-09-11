# Test for प.5.3.10

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_5_3_10.py'
spec = importlib.util.spec_from_file_location('P_5_3_10', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P_5_3_10'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra5310


def test_P_5_3_10():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

