# Sutra प.2.4.40: लिट्यन्यतरस्याम्
# (Samasa (compound formation)) — liwyanyatarasyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.40"
SUTRA_TEXT = "लिट्यन्यतरस्याम्"
SUTRA_DESC = "(Samasa (compound formation)) — liwyanyatarasyAm"


class Sutra2440:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

