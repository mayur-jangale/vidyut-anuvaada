# Sutra प.1.2.26: रलो व्युपधाद्धलादेः संश्च
# (Samjna (technical definitions)) — ralo vyupaDAdDalAdeH saMSca

from P_1_2 import apply_1_2_26

SUTRA_CODE = "प.1.2.26"
SUTRA_TEXT = "रलो व्युपधाद्धलादेः संश्च"
SUTRA_DESC = "(Samjna (technical definitions)) — ralo vyupaDAdDalAdeH saMSca"


class Sutra1226:
	def apply(self, word, pos):
		return apply_1_2_26(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-ralo:अग्निः'),
		('रामः', '', 'non-ralo:रामः'),
		('सीता', '', 'non-ralo:सीता'),
	]

