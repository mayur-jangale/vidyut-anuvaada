# Sutra प.7.3.13: दिशोऽमद्राणाम्
# (Taddhita (secondary derivations)) — diSo'madrARAm

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.13"
SUTRA_TEXT = "दिशोऽमद्राणाम्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — diSo'madrARAm"


class Sutra7313:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.13: अग्निः'),
		('रामः', '', 'प.7.3.13: रामः'),
		('सीता', '', 'प.7.3.13: सीता'),
	]

