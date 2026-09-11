# Sutra प.2.3.50: षष्ठी शेषे
# (Samasa (compound formation)) — zazWI Seze

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.50"
SUTRA_TEXT = "षष्ठी शेषे"
SUTRA_DESC = "(Samasa (compound formation)) — zazWI Seze"


class Sutra2350:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

