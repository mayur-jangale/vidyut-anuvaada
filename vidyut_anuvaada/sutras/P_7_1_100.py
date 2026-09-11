# Sutra प.7.1.100: ॠत इद्धातोः
# (Taddhita (secondary derivations)) — Fta idDAtoH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.100"
SUTRA_TEXT = "ॠत इद्धातोः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — Fta idDAtoH"


class Sutra71100:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.100: अग्निः'),
		('रामः', '', 'प.7.1.100: रामः'),
		('सीता', '', 'प.7.1.100: सीता'),
	]

