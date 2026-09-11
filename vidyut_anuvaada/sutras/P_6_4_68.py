# Sutra प.6.4.68: वाऽन्यस्य संयोगादेः
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.68"
SUTRA_TEXT = "वाऽन्यस्य संयोगादेः"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6468:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.68: अग्निः'),
		('रामः', '', 'प.6.4.68: रामः'),
		('सीता', '', 'प.6.4.68: सीता'),
	]

