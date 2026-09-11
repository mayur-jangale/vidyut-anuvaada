# Sutra प.1.2.22: पूङः क्त्वा च
# (Samjna (technical definitions)) — pUNaH ktvA ca

from P_1_2 import apply_1_2_22

SUTRA_CODE = "प.1.2.22"
SUTRA_TEXT = "पूङः क्त्वा च"
SUTRA_DESC = "(Samjna (technical definitions)) — pUNaH ktvA ca"


class Sutra1222:
	def apply(self, word, pos):
		return apply_1_2_22(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-pū:अग्निः'),
		('रामः', '', 'non-pū:रामः'),
		('सीता', '', 'non-pū:सीता'),
	]

