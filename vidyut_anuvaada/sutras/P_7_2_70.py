# Sutra प.7.2.70: ऋद्धनोः स्ये
# (Taddhita (secondary derivations)) — fdDanoH sye

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.70"
SUTRA_TEXT = "ऋद्धनोः स्ये"
SUTRA_DESC = "(Taddhita (secondary derivations)) — fdDanoH sye"


class Sutra7270:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.70: अग्निः'),
		('रामः', '', 'प.7.2.70: रामः'),
		('सीता', '', 'प.7.2.70: सीता'),
	]

