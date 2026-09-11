# Sutra प.7.3.72: क्सस्याचि
# (Taddhita (secondary derivations)) — ksasyAci

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.72"
SUTRA_TEXT = "क्सस्याचि"
SUTRA_DESC = "(Taddhita (secondary derivations)) — ksasyAci"


class Sutra7372:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.72: अग्निः'),
		('रामः', '', 'प.7.3.72: रामः'),
		('सीता', '', 'प.7.3.72: सीता'),
	]

