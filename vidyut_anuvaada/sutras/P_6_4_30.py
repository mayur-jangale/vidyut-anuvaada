# Sutra प.6.4.30: नाञ्चेः पूजायाम्
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.30"
SUTRA_TEXT = "नाञ्चेः पूजायाम्"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6430:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.30: अग्निः'),
		('रामः', '', 'प.6.4.30: रामः'),
		('सीता', '', 'प.6.4.30: सीता'),
	]

