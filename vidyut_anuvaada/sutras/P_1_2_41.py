# Sutra प.1.2.41: अपृक्त एकाल् प्रत्ययः
# (Samjna (technical definitions)) — apfkta ekAl pratyayaH

from P_1_2 import apply_1_2_41

SUTRA_CODE = "प.1.2.41"
SUTRA_TEXT = "अपृक्त एकाल् प्रत्ययः"
SUTRA_DESC = "(Samjna (technical definitions)) — apfkta ekAl pratyayaH"


class Sutra1241:
	def apply(self, word, pos):
		return apply_1_2_41(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-aprakta:अग्निः'),
		('रामः', '', 'non-aprakta:रामः'),
		('सीता', '', 'non-aprakta:सीता'),
	]

