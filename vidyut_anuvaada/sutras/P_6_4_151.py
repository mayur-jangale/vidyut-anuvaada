# Sutra प.6.4.151: आपत्यस्य च तद्धितेऽनाति
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.151"
SUTRA_TEXT = "आपत्यस्य च तद्धितेऽनाति"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra64151:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.151: अग्निः'),
		('रामः', '', 'प.6.4.151: रामः'),
		('सीता', '', 'प.6.4.151: सीता'),
	]

