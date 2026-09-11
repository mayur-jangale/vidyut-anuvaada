# Sutra प.6.2.86: छात्र्यादयः शालायाम्
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.86"
SUTRA_TEXT = "छात्र्यादयः शालायाम्"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6286:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.86: अग्निः'),
		('रामः', '', 'प.6.2.86: रामः'),
		('सीता', '', 'प.6.2.86: सीता'),
	]

