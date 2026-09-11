# Test for प.1.2.68

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_1_2_68.py'
spec = importlib.util.spec_from_file_location('P_1_2_68', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P_1_2_68'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra1268


def test_P_1_2_68():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

