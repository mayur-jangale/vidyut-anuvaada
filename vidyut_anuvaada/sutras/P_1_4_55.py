# Sutra प.1.4.55: तत्प्रयोजको हेतुश्च
# (Samjna (technical definitions)) — tatprayojako hetuSca

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.55"
SUTRA_TEXT = "तत्प्रयोजको हेतुश्च"
SUTRA_DESC = "(Samjna (technical definitions)) — tatprayojako hetuSca"


class Sutra1455:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_55
		return apply_1_4_55(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-hetu:अग्निः'),
		('रामः', '', 'not-hetu:रामः'),
		('सीता', '', 'not-hetu:सीता'),
	]

