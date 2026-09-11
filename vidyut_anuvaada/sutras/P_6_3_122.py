# Sutra प.6.3.122: उपसर्गस्य घञ्यमनुष्ये बहुलम्
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.122"
SUTRA_TEXT = "उपसर्गस्य घञ्यमनुष्ये बहुलम्"
SUTRA_DESC = "final-sandhi — continued"


class Sutra63122:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.122: अग्निः'),
		('रामः', '', 'प.6.3.122: रामः'),
		('सीता', '', 'प.6.3.122: सीता'),
	]

