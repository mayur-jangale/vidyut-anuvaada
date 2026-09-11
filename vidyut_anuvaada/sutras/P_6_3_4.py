# Sutra प.6.3.4: मनसः संज्ञायाम्
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.4"
SUTRA_TEXT = "मनसः संज्ञायाम्"
SUTRA_DESC = "final-sandhi — continued"


class Sutra634:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.4: अग्निः'),
		('रामः', '', 'प.6.3.4: रामः'),
		('सीता', '', 'प.6.3.4: सीता'),
	]

