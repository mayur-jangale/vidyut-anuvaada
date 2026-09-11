# Sutra प.6.3.114: संहितायाम्
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.114"
SUTRA_TEXT = "संहितायाम्"
SUTRA_DESC = "final-sandhi — continued"


class Sutra63114:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.114: अग्निः'),
		('रामः', '', 'प.6.3.114: रामः'),
		('सीता', '', 'प.6.3.114: सीता'),
	]

