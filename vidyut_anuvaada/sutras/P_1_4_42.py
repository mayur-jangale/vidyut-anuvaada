# Sutra प.1.4.42: साधकतमं करणम्
# (Samjna (technical definitions)) — sADakatamaM karaRam

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.42"
SUTRA_TEXT = "साधकतमं करणम्"
SUTRA_DESC = "(Samjna (technical definitions)) — sADakatamaM karaRam"


class Sutra1442:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_42
		return apply_1_4_42(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-sADakatama-karaNam:अग्निः'),
		('रामः', '', 'not-sADakatama-karaNam:रामः'),
		('सीता', '', 'not-sADakatama-karaNam:सीता'),
	]

