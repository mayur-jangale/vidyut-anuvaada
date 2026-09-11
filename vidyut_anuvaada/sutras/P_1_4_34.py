# Sutra प.1.4.34: श्लाघह्नुङ्स्थाशपां ज्ञीप्स्यमानः
# (Samjna (technical definitions)) — SlAGahnuNsTASapAM jYIpsyamAnaH

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.34"
SUTRA_TEXT = "श्लाघह्नुङ्स्थाशपां ज्ञीप्स्यमानः"
SUTRA_DESC = "(Samjna (technical definitions)) — SlAGahnuNsTASapAM jYIpsyamAnaH"


class Sutra1434:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_34
		return apply_1_4_34(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-SlAGhA-sampradAnam:अग्निः'),
		('रामः', '', 'not-SlAGhA-sampradAnam:रामः'),
		('सीता', '', 'not-SlAGhA-sampradAnam:सीता'),
	]

