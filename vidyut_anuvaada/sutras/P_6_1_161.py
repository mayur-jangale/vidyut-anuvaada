# Sutra प.6.1.161: अनुदात्तस्य च यत्रोदात्तलोपः
# sandhi-sūtra प.6.1.161

from P_6_1 import apply_6_1_161

SUTRA_CODE = "प.6.1.161"
SUTRA_TEXT = "अनुदात्तस्य च यत्रोदात्तलोपः"
SUTRA_DESC = "sandhi-sūtra प.6.1.161"


class Sutra61161:
	def apply(self, word, pos):
		return apply_6_1_161(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.161:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.161:marker=padartha;input=रामः'),
		('सीता', '', '6.1.161:marker=padartha;input=सीता'),
	]
