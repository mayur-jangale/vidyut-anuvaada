# Sutra प.1.4.53: हृक्रोरन्यतरस्याम्
# (Samjna (technical definitions)) — hfkroranyatarasyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.53"
SUTRA_TEXT = "हृक्रोरन्यतरस्याम्"
SUTRA_DESC = "(Samjna (technical definitions)) — hfkroranyatarasyAm"


class Sutra1453:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_53
		return apply_1_4_53(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-hR-kR:अग्निः'),
		('रामः', '', 'not-hR-kR:रामः'),
		('सीता', '', 'not-hR-kR:सीता'),
	]

