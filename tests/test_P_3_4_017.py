# Test for प17

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_3_4_017.py'
spec = importlib.util.spec_from_file_location('P17', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P17'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra3417


def test_P17():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

