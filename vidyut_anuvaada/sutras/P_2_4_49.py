# Sutra प.2.4.49: गाङ् लिटि
# (Samasa (compound formation)) — gAN liwi

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.49"
SUTRA_TEXT = "गाङ् लिटि"
SUTRA_DESC = "(Samasa (compound formation)) — gAN liwi"


class Sutra2449:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

