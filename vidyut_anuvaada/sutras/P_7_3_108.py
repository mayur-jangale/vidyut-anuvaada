# Sutra प.7.3.108: ह्रस्वस्य गुणः
# (Taddhita (secondary derivations)) — hrasvasya guRaH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.108"
SUTRA_TEXT = "ह्रस्वस्य गुणः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — hrasvasya guRaH"


class Sutra73108:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.108: अग्निः'),
		('रामः', '', 'प.7.3.108: रामः'),
		('सीता', '', 'प.7.3.108: सीता'),
	]

