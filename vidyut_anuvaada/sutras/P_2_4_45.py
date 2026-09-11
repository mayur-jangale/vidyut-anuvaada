# Sutra प.2.4.45: इणो गा लुङि
# (Samasa (compound formation)) — iRo gA luNi

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.45"
SUTRA_TEXT = "इणो गा लुङि"
SUTRA_DESC = "(Samasa (compound formation)) — iRo gA luNi"


class Sutra2445:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

