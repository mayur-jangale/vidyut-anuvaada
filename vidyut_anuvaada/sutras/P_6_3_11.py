# Sutra प.6.3.11: मध्याद्गुरौ
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.11"
SUTRA_TEXT = "मध्याद्गुरौ"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6311:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.11: अग्निः'),
		('रामः', '', 'प.6.3.11: रामः'),
		('सीता', '', 'प.6.3.11: सीता'),
	]

