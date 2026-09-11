# Sutra प.6.3.81: अव्ययीभावे चाकाले
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.81"
SUTRA_TEXT = "अव्ययीभावे चाकाले"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6381:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.81: अग्निः'),
		('रामः', '', 'प.6.3.81: रामः'),
		('सीता', '', 'प.6.3.81: सीता'),
	]

