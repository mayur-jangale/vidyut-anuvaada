# Sutra प.6.2.158: आक्रोशे च
# (Sandhi (euphonic combination)) — AkroSe ca

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.158"
SUTRA_TEXT = "आक्रोशे च"
SUTRA_DESC = "(Sandhi (euphonic combination)) — AkroSe ca"


class Sutra62158:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.158: अग्निः'),
		('रामः', '', 'प.6.2.158: रामः'),
		('सीता', '', 'प.6.2.158: सीता'),
	]

