# Sutra प.2.4.82: अव्ययादाप्सुपः
# (Samasa (compound formation)) — avyayAdApsupaH

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.82"
SUTRA_TEXT = "अव्ययादाप्सुपः"
SUTRA_DESC = "(Samasa (compound formation)) — avyayAdApsupaH"


class Sutra2482:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

