# Sutra प.6.2.141: देवताद्वन्द्वे च
# (Sandhi (euphonic combination)) — devatAdvandve ca

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.141"
SUTRA_TEXT = "देवताद्वन्द्वे च"
SUTRA_DESC = "(Sandhi (euphonic combination)) — devatAdvandve ca"


class Sutra62141:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.141: अग्निः'),
		('रामः', '', 'प.6.2.141: रामः'),
		('सीता', '', 'प.6.2.141: सीता'),
	]

