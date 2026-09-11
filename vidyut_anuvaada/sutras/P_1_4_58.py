# Sutra प.1.4.58: प्रादयः
# (Samjna (technical definitions)) — prAdayaH

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.58"
SUTRA_TEXT = "प्रादयः"
SUTRA_DESC = "(Samjna (technical definitions)) — prAdayaH"


class Sutra1458:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_58
		return apply_1_4_58(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-prAdi:अग्निः'),
		('रामः', '', 'not-prAdi:रामः'),
		('सीता', '', 'not-prAdi:सीता'),
	]

