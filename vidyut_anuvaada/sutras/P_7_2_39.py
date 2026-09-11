# Sutra प.7.2.39: न लिङि
# (Taddhita (secondary derivations)) — na liNi

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.39"
SUTRA_TEXT = "न लिङि"
SUTRA_DESC = "(Taddhita (secondary derivations)) — na liNi"


class Sutra7239:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.39: अग्निः'),
		('रामः', '', 'प.7.2.39: रामः'),
		('सीता', '', 'प.7.2.39: सीता'),
	]

