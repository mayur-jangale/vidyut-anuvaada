# Sutra प.6.1.144: अपरस्पराः क्रियासातत्ये
# sandhi-sūtra प.6.1.144

from P_6_1 import apply_6_1_144

SUTRA_CODE = "प.6.1.144"
SUTRA_TEXT = "अपरस्पराः क्रियासातत्ये"
SUTRA_DESC = "sandhi-sūtra प.6.1.144"


class Sutra61144:
	def apply(self, word, pos):
		return apply_6_1_144(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.144:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.144:marker=padartha;input=रामः'),
		('सीता', '', '6.1.144:marker=padartha;input=सीता'),
	]
