# Sutra प.7.3.14: प्राचां ग्रामनगराणाम्
# (Taddhita (secondary derivations)) — prAcAM grAmanagarARAm

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.14"
SUTRA_TEXT = "प्राचां ग्रामनगराणाम्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — prAcAM grAmanagarARAm"


class Sutra7314:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.14: अग्निः'),
		('रामः', '', 'प.7.3.14: रामः'),
		('सीता', '', 'प.7.3.14: सीता'),
	]

