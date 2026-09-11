# Sutra प.7.1.14: सर्वनाम्नः स्मै
# (Taddhita (secondary derivations)) — sarvanAmnaH smE

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.14"
SUTRA_TEXT = "सर्वनाम्नः स्मै"
SUTRA_DESC = "(Taddhita (secondary derivations)) — sarvanAmnaH smE"


class Sutra7114:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.14: अग्निः'),
		('रामः', '', 'प.7.1.14: रामः'),
		('सीता', '', 'प.7.1.14: सीता'),
	]

