# Sutra प.2.4.55: वा लिटि
# (Samasa (compound formation)) — vA liwi

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.55"
SUTRA_TEXT = "वा लिटि"
SUTRA_DESC = "(Samasa (compound formation)) — vA liwi"


class Sutra2455:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

