# Sutra प.1.4.67: पुरोऽव्ययम्
# (Samjna (technical definitions)) — puro'vyayam

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.67"
SUTRA_TEXT = "पुरोऽव्ययम्"
SUTRA_DESC = "(Samjna (technical definitions)) — puro'vyayam"


class Sutra1467:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_67
		return apply_1_4_67(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-purA:अग्निः'),
		('रामः', '', 'not-purA:रामः'),
		('सीता', '', 'not-purA:सीता'),
	]

