# Sutra प.6.2.100: अरिष्टगौडपूर्वे च
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.100"
SUTRA_TEXT = "अरिष्टगौडपूर्वे च"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra62100:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.100: अग्निः'),
		('रामः', '', 'प.6.2.100: रामः'),
		('सीता', '', 'प.6.2.100: सीता'),
	]

