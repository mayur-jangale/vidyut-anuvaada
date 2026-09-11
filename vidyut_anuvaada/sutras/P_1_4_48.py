# Sutra प.1.4.48: उपान्वध्याङ्वसः
# (Samjna (technical definitions)) — upAnvaDyANvasaH

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.48"
SUTRA_TEXT = "उपान्वध्याङ्वसः"
SUTRA_DESC = "(Samjna (technical definitions)) — upAnvaDyANvasaH"


class Sutra1448:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_48
		return apply_1_4_48(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-upAnva-karman:अग्निः'),
		('रामः', '', 'not-upAnva-karman:रामः'),
		('सीता', '', 'not-upAnva-karman:सीता'),
	]

