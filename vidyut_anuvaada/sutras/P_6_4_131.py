# Sutra प.6.4.131: वसोः सम्प्रसारणम्
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.131"
SUTRA_TEXT = "वसोः सम्प्रसारणम्"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra64131:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.131: अग्निः'),
		('रामः', '', 'प.6.4.131: रामः'),
		('सीता', '', 'प.6.4.131: सीता'),
	]

