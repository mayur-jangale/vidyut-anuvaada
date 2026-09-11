# Test for प95

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_3_4_095.py'
spec = importlib.util.spec_from_file_location('P95', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P95'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra3495


def test_P95():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

