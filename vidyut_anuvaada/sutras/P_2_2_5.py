# Sutra प.2.2.5: कालाः परिमाणिना
# (Samasa (compound formation)) — kAlAH parimARinA

from sutra_engines import apply_general

SUTRA_CODE = "प.2.2.5"
SUTRA_TEXT = "कालाः परिमाणिना"
SUTRA_DESC = "(Samasa (compound formation)) — kAlAH parimARinA"


class Sutra225:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

