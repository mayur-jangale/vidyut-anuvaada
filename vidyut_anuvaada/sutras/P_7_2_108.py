# Sutra प.7.2.108: इदमो मः
# (Taddhita (secondary derivations)) — idamo maH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.108"
SUTRA_TEXT = "इदमो मः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — idamo maH"


class Sutra72108:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.108: अग्निः'),
		('रामः', '', 'प.7.2.108: रामः'),
		('सीता', '', 'प.7.2.108: सीता'),
	]

