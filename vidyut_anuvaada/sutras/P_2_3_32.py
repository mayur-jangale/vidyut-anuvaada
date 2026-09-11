# Sutra प.2.3.32: पृथग्विनानानाभिस्तृतीयाऽन्यतरस्याम्
# (Samasa (compound formation)) — pfTagvinAnAnABistftIyA'nyatarasyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.32"
SUTRA_TEXT = "पृथग्विनानानाभिस्तृतीयाऽन्यतरस्याम्"
SUTRA_DESC = "(Samasa (compound formation)) — pfTagvinAnAnABistftIyA'nyatarasyAm"


class Sutra2332:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

