# Sutra प.6.4.8: सर्वनामस्थाने चासम्बुद्धौ
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.8"
SUTRA_TEXT = "सर्वनामस्थाने चासम्बुद्धौ"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra648:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.8: अग्निः'),
		('रामः', '', 'प.6.4.8: रामः'),
		('सीता', '', 'प.6.4.8: सीता'),
	]

