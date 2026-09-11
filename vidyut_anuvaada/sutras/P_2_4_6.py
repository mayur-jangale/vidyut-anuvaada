# Sutra प.2.4.6: जातिरप्राणिनाम्
# (Samasa (compound formation)) — jAtiraprARinAm

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.6"
SUTRA_TEXT = "जातिरप्राणिनाम्"
SUTRA_DESC = "(Samasa (compound formation)) — jAtiraprARinAm"


class Sutra246:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

