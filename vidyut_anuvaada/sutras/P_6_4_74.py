# Sutra प.6.4.74: न माङ्योगे
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.74"
SUTRA_TEXT = "न माङ्योगे"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6474:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.74: अग्निः'),
		('रामः', '', 'प.6.4.74: रामः'),
		('सीता', '', 'प.6.4.74: सीता'),
	]

