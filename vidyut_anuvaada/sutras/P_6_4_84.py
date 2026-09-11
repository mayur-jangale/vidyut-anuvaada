# Sutra प.6.4.84: वर्षाभ्वश्च
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.84"
SUTRA_TEXT = "वर्षाभ्वश्च"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6484:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.84: अग्निः'),
		('रामः', '', 'प.6.4.84: रामः'),
		('सीता', '', 'प.6.4.84: सीता'),
	]

