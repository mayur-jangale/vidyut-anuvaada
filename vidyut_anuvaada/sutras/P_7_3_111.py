# Sutra प.7.3.111: घेर्ङिति
# (Taddhita (secondary derivations)) — GerNiti

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.111"
SUTRA_TEXT = "घेर्ङिति"
SUTRA_DESC = "(Taddhita (secondary derivations)) — GerNiti"


class Sutra73111:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.111: अग्निः'),
		('रामः', '', 'प.7.3.111: रामः'),
		('सीता', '', 'प.7.3.111: सीता'),
	]

