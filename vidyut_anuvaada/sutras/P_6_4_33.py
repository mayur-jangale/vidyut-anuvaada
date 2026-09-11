# Sutra प.6.4.33: भञ्जेश्च चिणि
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.33"
SUTRA_TEXT = "भञ्जेश्च चिणि"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6433:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.33: अग्निः'),
		('रामः', '', 'प.6.4.33: रामः'),
		('सीता', '', 'प.6.4.33: सीता'),
	]

