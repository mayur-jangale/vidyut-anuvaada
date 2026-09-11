# Sutra प.6.2.128: पललसूपशाकं मिश्रे
# (Sandhi (euphonic combination)) — palalasUpaSAkaM miSre

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.128"
SUTRA_TEXT = "पललसूपशाकं मिश्रे"
SUTRA_DESC = "(Sandhi (euphonic combination)) — palalasUpaSAkaM miSre"


class Sutra62128:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.128: अग्निः'),
		('रामः', '', 'प.6.2.128: रामः'),
		('सीता', '', 'प.6.2.128: सीता'),
	]

