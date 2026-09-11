# Sutra प.2.3.72: तुल्यार्थैरतुलोपमाभ्यां तृतीयाऽन्यतरस्याम्
# (Samasa (compound formation)) — tulyArTEratulopamAByAM tftIyA'nyatarasyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.72"
SUTRA_TEXT = "तुल्यार्थैरतुलोपमाभ्यां तृतीयाऽन्यतरस्याम्"
SUTRA_DESC = "(Samasa (compound formation)) — tulyArTEratulopamAByAM tftIyA'nyatarasyAm"


class Sutra2372:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

