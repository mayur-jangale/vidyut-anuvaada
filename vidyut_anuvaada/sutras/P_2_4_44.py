# Sutra प.2.4.44: आत्मनेपदेष्वन्यतरस्याम्
# (Samasa (compound formation)) — AtmanepadezvanyatarasyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.44"
SUTRA_TEXT = "आत्मनेपदेष्वन्यतरस्याम्"
SUTRA_DESC = "(Samasa (compound formation)) — AtmanepadezvanyatarasyAm"


class Sutra2444:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

