# Sutra प.6.1.146: आस्पदं प्रतिष्ठायाम्
# sandhi-sūtra प.6.1.146

from P_6_1 import apply_6_1_146

SUTRA_CODE = "प.6.1.146"
SUTRA_TEXT = "आस्पदं प्रतिष्ठायाम्"
SUTRA_DESC = "sandhi-sūtra प.6.1.146"


class Sutra61146:
	def apply(self, word, pos):
		return apply_6_1_146(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.146:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.146:marker=padartha;input=रामः'),
		('सीता', '', '6.1.146:marker=padartha;input=सीता'),
	]
