# Sutra प.7.2.46: निरः कुषः
# (Taddhita (secondary derivations)) — niraH kuzaH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.46"
SUTRA_TEXT = "निरः कुषः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — niraH kuzaH"


class Sutra7246:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.46: अग्निः'),
		('रामः', '', 'प.7.2.46: रामः'),
		('सीता', '', 'प.7.2.46: सीता'),
	]

