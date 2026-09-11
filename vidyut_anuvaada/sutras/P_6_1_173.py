# Sutra प.6.1.173: शतुरनुमो नद्यजादी
# sandhi-sūtra प.6.1.173

from P_6_1 import apply_6_1_173

SUTRA_CODE = "प.6.1.173"
SUTRA_TEXT = "शतुरनुमो नद्यजादी"
SUTRA_DESC = "sandhi-sūtra प.6.1.173"


class Sutra61173:
	def apply(self, word, pos):
		return apply_6_1_173(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.173:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.173:marker=padartha;input=रामः'),
		('सीता', '', '6.1.173:marker=padartha;input=सीता'),
	]
