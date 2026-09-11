# Sutra प.8.4.28: उपसर्गाद् बहुलम्
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.28"
SUTRA_TEXT = "उपसर्गाद् बहुलम्"
SUTRA_DESC = "final transformations — continued"


class Sutra8428:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.28: अग्निः'),
		('रामः', '', 'प.8.4.28: रामः'),
		('सीता', '', 'प.8.4.28: सीता'),
	]

