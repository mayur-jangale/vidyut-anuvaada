# Sutra प.7.1.63: रभेरशब्लिटोः
# (Taddhita (secondary derivations)) — raBeraSabliwoH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.63"
SUTRA_TEXT = "रभेरशब्लिटोः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — raBeraSabliwoH"


class Sutra7163:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.63: अग्निः'),
		('रामः', '', 'प.7.1.63: रामः'),
		('सीता', '', 'प.7.1.63: सीता'),
	]

