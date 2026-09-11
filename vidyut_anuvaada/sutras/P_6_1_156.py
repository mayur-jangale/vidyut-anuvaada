# Sutra प.6.1.156: कारस्करो वृक्षः
# sandhi-sūtra प.6.1.156

from P_6_1 import apply_6_1_156

SUTRA_CODE = "प.6.1.156"
SUTRA_TEXT = "कारस्करो वृक्षः"
SUTRA_DESC = "sandhi-sūtra प.6.1.156"


class Sutra61156:
	def apply(self, word, pos):
		return apply_6_1_156(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.156:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.156:marker=padartha;input=रामः'),
		('सीता', '', '6.1.156:marker=padartha;input=सीता'),
	]
