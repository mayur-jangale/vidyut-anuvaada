# Sutra प.6.3.32: मातरपितरावुदीचाम्
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.32"
SUTRA_TEXT = "मातरपितरावुदीचाम्"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6332:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.32: अग्निः'),
		('रामः', '', 'प.6.3.32: रामः'),
		('सीता', '', 'प.6.3.32: सीता'),
	]

