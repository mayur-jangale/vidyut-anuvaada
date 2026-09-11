# Sutra प.6.1.119: अङ्ग इत्यादौ च
# sandhi-sūtra प.6.1.119

from P_6_1 import apply_6_1_119

SUTRA_CODE = "प.6.1.119"
SUTRA_TEXT = "अङ्ग इत्यादौ च"
SUTRA_DESC = "sandhi-sūtra प.6.1.119"


class Sutra61119:
	def apply(self, word, pos):
		return apply_6_1_119(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.119:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.119:marker=padartha;input=रामः'),
		('सीता', '', '6.1.119:marker=padartha;input=सीता'),
	]
