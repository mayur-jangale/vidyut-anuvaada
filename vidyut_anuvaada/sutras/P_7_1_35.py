# Sutra प.7.1.35: तुह्योस्तातङ्ङाशिष्यन्यतरस्याम्
# (Taddhita (secondary derivations)) — tuhyostAtaNNASizyanyatarasyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.35"
SUTRA_TEXT = "तुह्योस्तातङ्ङाशिष्यन्यतरस्याम्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — tuhyostAtaNNASizyanyatarasyAm"


class Sutra7135:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.35: अग्निः'),
		('रामः', '', 'प.7.1.35: रामः'),
		('सीता', '', 'प.7.1.35: सीता'),
	]

