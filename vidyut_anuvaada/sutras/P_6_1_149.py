# Sutra प.6.1.149: अपस्करो रथाङ्गम्
# sandhi-sūtra प.6.1.149

from P_6_1 import apply_6_1_149

SUTRA_CODE = "प.6.1.149"
SUTRA_TEXT = "अपस्करो रथाङ्गम्"
SUTRA_DESC = "sandhi-sūtra प.6.1.149"


class Sutra61149:
	def apply(self, word, pos):
		return apply_6_1_149(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.149:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.149:marker=padartha;input=रामः'),
		('सीता', '', '6.1.149:marker=padartha;input=सीता'),
	]
