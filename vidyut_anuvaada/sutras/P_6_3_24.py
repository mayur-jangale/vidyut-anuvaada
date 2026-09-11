# Sutra प.6.3.24: विभाषा स्वसृपत्योः
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.24"
SUTRA_TEXT = "विभाषा स्वसृपत्योः"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6324:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.24: अग्निः'),
		('रामः', '', 'प.6.3.24: रामः'),
		('सीता', '', 'प.6.3.24: सीता'),
	]

