# Sutra प.1.4.77: नित्यं हस्ते पाणावुपयमने
# (Samjna (technical definitions)) — nityaM haste pARAvupayamane

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.77"
SUTRA_TEXT = "नित्यं हस्ते पाणावुपयमने"
SUTRA_DESC = "(Samjna (technical definitions)) — nityaM haste pARAvupayamane"


class Sutra1477:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_77
		return apply_1_4_77(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-hasta:अग्निः'),
		('रामः', '', 'not-hasta:रामः'),
		('सीता', '', 'not-hasta:सीता'),
	]

