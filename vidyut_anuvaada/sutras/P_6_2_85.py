# Sutra प.6.2.85: घोषादिषु च
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.85"
SUTRA_TEXT = "घोषादिषु च"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6285:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.85: अग्निः'),
		('रामः', '', 'प.6.2.85: रामः'),
		('सीता', '', 'प.6.2.85: सीता'),
	]

