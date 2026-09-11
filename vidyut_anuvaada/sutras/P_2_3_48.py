# Sutra प.2.3.48: सामन्त्रितम्
# (Samasa (compound formation)) — sAmantritam

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.48"
SUTRA_TEXT = "सामन्त्रितम्"
SUTRA_DESC = "(Samasa (compound formation)) — sAmantritam"


class Sutra2348:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

