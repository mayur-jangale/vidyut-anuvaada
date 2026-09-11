# Sutra प.6.4.29: अवोदैधौद्मप्रश्रथहिमश्रथाः
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.29"
SUTRA_TEXT = "अवोदैधौद्मप्रश्रथहिमश्रथाः"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6429:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.29: अग्निः'),
		('रामः', '', 'प.6.4.29: रामः'),
		('सीता', '', 'प.6.4.29: सीता'),
	]

