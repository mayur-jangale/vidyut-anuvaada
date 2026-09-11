# Sutra प.2.3.49: एकवचनं संबुद्धिः
# (Samasa (compound formation)) — ekavacanaM saMbudDiH

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.49"
SUTRA_TEXT = "एकवचनं संबुद्धिः"
SUTRA_DESC = "(Samasa (compound formation)) — ekavacanaM saMbudDiH"


class Sutra2349:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

