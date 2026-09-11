# Sutra प.2.4.71: सुपो धातुप्रातिपदिकयोः
# (Samasa (compound formation)) — supo DAtuprAtipadikayoH

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.71"
SUTRA_TEXT = "सुपो धातुप्रातिपदिकयोः"
SUTRA_DESC = "(Samasa (compound formation)) — supo DAtuprAtipadikayoH"


class Sutra2471:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

