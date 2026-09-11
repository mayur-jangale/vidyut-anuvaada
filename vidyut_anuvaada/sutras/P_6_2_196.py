# Sutra प.6.2.196: विभाषोत्पुच्छे
# (Sandhi (euphonic combination)) — viBAzotpucCe

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.196"
SUTRA_TEXT = "विभाषोत्पुच्छे"
SUTRA_DESC = "(Sandhi (euphonic combination)) — viBAzotpucCe"


class Sutra62196:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.196: अग्निः'),
		('रामः', '', 'प.6.2.196: रामः'),
		('सीता', '', 'प.6.2.196: सीता'),
	]

