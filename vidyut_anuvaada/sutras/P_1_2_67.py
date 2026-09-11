# Sutra प.1.2.67: पुमान् स्त्रिया
# (Samjna (technical definitions)) — pumAn striyA

from P_1_2 import apply_1_2_67

SUTRA_CODE = "प.1.2.67"
SUTRA_TEXT = "पुमान् स्त्रिया"
SUTRA_DESC = "(Samjna (technical definitions)) — pumAn striyA"


class Sutra1267:
	def apply(self, word, pos):
		return apply_1_2_67(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-pumān:अग्निः'),
		('रामः', '', 'non-pumān:रामः'),
		('सीता', '', 'non-pumān:सीता'),
	]

