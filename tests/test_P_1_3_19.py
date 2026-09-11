# Test for P_1_3_19

import importlib.util, pathlib, pytest, sys

SRC = pathlib.Path(__file__).resolve().parent.parent / 'vidyut_anuvaada' / 'sutras' / 'P_1_3_19.py'
spec = importlib.util.spec_from_file_location('P_1_3_19', SRC)
mod = importlib.util.module_from_spec(spec)
sys.modules['P_1_3_19'] = mod
spec.loader.exec_module(mod)
cls = mod.Sutra1319


def test_P_1_3_19():
	for w, p, expected in cls.EXAMPLES:
		result = cls().apply(w, p)
		assert result == expected, f"FAIL: {w} ({p}) -> {result}, expected {expected}"

