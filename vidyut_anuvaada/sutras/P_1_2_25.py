# Sutra प.1.2.25: तृषिमृषिकृशेः काश्यपस्य
# (Samjna (technical definitions)) — tfzimfzikfSeH kASyapasya

from P_1_2 import apply_1_2_25

SUTRA_CODE = "प.1.2.25"
SUTRA_TEXT = "तृषिमृषिकृशेः काश्यपस्य"
SUTRA_DESC = "(Samjna (technical definitions)) — tfzimfzikfSeH kASyapasya"


class Sutra1225:
	def apply(self, word, pos):
		return apply_1_2_25(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'default-rule:अग्निः'),
		('रामः', '', 'default-rule:रामः'),
		('सीता', '', 'default-rule:सीता'),
	]

