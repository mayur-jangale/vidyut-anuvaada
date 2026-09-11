# Sutra प.7.3.116: ङेराम्नद्याम्नीभ्यः
# (Taddhita (secondary derivations)) — NerAmnadyAmnIByaH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.116"
SUTRA_TEXT = "ङेराम्नद्याम्नीभ्यः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — NerAmnadyAmnIByaH"


class Sutra73116:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.116: अग्निः'),
		('रामः', '', 'प.7.3.116: रामः'),
		('सीता', '', 'प.7.3.116: सीता'),
	]

