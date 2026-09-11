# Sutra प.2.4.52: अस्तेर्भूः
# (Samasa (compound formation)) — asterBUH

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.52"
SUTRA_TEXT = "अस्तेर्भूः"
SUTRA_DESC = "(Samasa (compound formation)) — asterBUH"


class Sutra2452:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

