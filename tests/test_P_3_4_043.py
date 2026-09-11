# Test for प43

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_3_4_043.py'
spec = importlib.util.spec_from_file_location('P43', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P43'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra3443


def test_P43():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

