# Sutra प.6.1.216: त्यागरागहासकुहश्वठक्रथानाम्
# sandhi-sūtra प.6.1.216

from P_6_1 import apply_6_1_216

SUTRA_CODE = "प.6.1.216"
SUTRA_TEXT = "त्यागरागहासकुहश्वठक्रथानाम्"
SUTRA_DESC = "sandhi-sūtra प.6.1.216"


class Sutra61216:
	def apply(self, word, pos):
		return apply_6_1_216(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.216:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.216:marker=padartha;input=रामः'),
		('सीता', '', '6.1.216:marker=padartha;input=सीता'),
	]
