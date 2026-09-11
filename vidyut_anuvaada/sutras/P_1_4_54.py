# Sutra प.1.4.54: स्वतन्त्रः कर्ता
# (Samjna (technical definitions)) — svatantraH kartA

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.54"
SUTRA_TEXT = "स्वतन्त्रः कर्ता"
SUTRA_DESC = "(Samjna (technical definitions)) — svatantraH kartA"


class Sutra1454:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_54
		return apply_1_4_54(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-kartA:अग्निः'),
		('रामः', '', 'not-kartA:रामः'),
		('सीता', '', 'not-kartA:सीता'),
	]

