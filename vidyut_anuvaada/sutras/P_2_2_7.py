# Sutra प.2.2.7: ईषदकृता
# (Samasa (compound formation)) — IzadakftA

from sutra_engines import apply_general

SUTRA_CODE = "प.2.2.7"
SUTRA_TEXT = "ईषदकृता"
SUTRA_DESC = "(Samasa (compound formation)) — IzadakftA"


class Sutra227:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

