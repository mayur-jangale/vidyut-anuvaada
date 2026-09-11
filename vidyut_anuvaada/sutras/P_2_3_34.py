# Sutra प.2.3.34: दूरान्तिकार्थैः षष्ठ्यन्यतरस्याम्
# (Samasa (compound formation)) — dUrAntikArTEH zazWyanyatarasyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.34"
SUTRA_TEXT = "दूरान्तिकार्थैः षष्ठ्यन्यतरस्याम्"
SUTRA_DESC = "(Samasa (compound formation)) — dUrAntikArTEH zazWyanyatarasyAm"


class Sutra2334:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

