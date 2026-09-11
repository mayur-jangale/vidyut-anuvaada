# Sutra प.6.1.221: ईवत्याः
# sandhi-sūtra प.6.1.221

from P_6_1 import apply_6_1_221

SUTRA_CODE = "प.6.1.221"
SUTRA_TEXT = "ईवत्याः"
SUTRA_DESC = "sandhi-sūtra प.6.1.221"


class Sutra61221:
	def apply(self, word, pos):
		return apply_6_1_221(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.221:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.221:marker=padartha;input=रामः'),
		('सीता', '', '6.1.221:marker=padartha;input=सीता'),
	]
