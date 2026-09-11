# Sutra प.7.3.57: सन्लिटोर्जेः
# (Taddhita (secondary derivations)) — sanliworjeH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.57"
SUTRA_TEXT = "सन्लिटोर्जेः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — sanliworjeH"


class Sutra7357:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.57: अग्निः'),
		('रामः', '', 'प.7.3.57: रामः'),
		('सीता', '', 'प.7.3.57: सीता'),
	]

