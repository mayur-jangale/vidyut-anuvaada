# Sutra प.7.2.11: श्र्युकः किति
# (Taddhita (secondary derivations)) — SryukaH kiti

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.11"
SUTRA_TEXT = "श्र्युकः किति"
SUTRA_DESC = "(Taddhita (secondary derivations)) — SryukaH kiti"


class Sutra7211:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.11: अग्निः'),
		('रामः', '', 'प.7.2.11: रामः'),
		('सीता', '', 'प.7.2.11: सीता'),
	]

