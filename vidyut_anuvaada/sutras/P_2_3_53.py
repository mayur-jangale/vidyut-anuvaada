# Sutra प.2.3.53: कृञः प्रतियत्ने
# (Samasa (compound formation)) — kfYaH pratiyatne

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.53"
SUTRA_TEXT = "कृञः प्रतियत्ने"
SUTRA_DESC = "(Samasa (compound formation)) — kfYaH pratiyatne"


class Sutra2353:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

