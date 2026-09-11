# Sutra प.7.3.87: नाभ्यस्तस्याचि पिति सार्वधातुके
# (Taddhita (secondary derivations)) — nAByastasyAci piti sArvaDAtuke

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.87"
SUTRA_TEXT = "नाभ्यस्तस्याचि पिति सार्वधातुके"
SUTRA_DESC = "(Taddhita (secondary derivations)) — nAByastasyAci piti sArvaDAtuke"


class Sutra7387:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.87: अग्निः'),
		('रामः', '', 'प.7.3.87: रामः'),
		('सीता', '', 'प.7.3.87: सीता'),
	]

