# Sutra प.6.1.67: वेरपृक्तस्य
# sandhi-sūtra प.6.1.67

from P_6_1 import apply_6_1_67

SUTRA_CODE = "प.6.1.67"
SUTRA_TEXT = "वेरपृक्तस्य"
SUTRA_DESC = "sandhi-sūtra प.6.1.67"


class Sutra6167:
	def apply(self, word, pos):
		return apply_6_1_67(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.67:input=अग्निः'),
		('रामः', '', '6.1.67:input=रामः'),
		('सीता', '', '6.1.67:input=सीता'),
	]
