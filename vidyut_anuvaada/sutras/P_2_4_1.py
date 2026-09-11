# Sutra प.2.4.1: द्विगुरेकवचनम्
# (Samasa (compound formation)) — dvigurekavacanam

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.1"
SUTRA_TEXT = "द्विगुरेकवचनम्"
SUTRA_DESC = "(Samasa (compound formation)) — dvigurekavacanam"


class Sutra241:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

