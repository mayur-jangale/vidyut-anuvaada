# Sutra प.2.3.5: कालाध्वनोरत्यन्तसंयोगे
# (Samasa (compound formation)) — kAlADvanoratyantasaMyoge

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.5"
SUTRA_TEXT = "कालाध्वनोरत्यन्तसंयोगे"
SUTRA_DESC = "(Samasa (compound formation)) — kAlADvanoratyantasaMyoge"


class Sutra235:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

