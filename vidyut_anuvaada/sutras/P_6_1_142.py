# Sutra प.6.1.142: अपाच्चतुष्पाच्छकुनिष्वालेखने
# sandhi-sūtra प.6.1.142

from P_6_1 import apply_6_1_142

SUTRA_CODE = "प.6.1.142"
SUTRA_TEXT = "अपाच्चतुष्पाच्छकुनिष्वालेखने"
SUTRA_DESC = "sandhi-sūtra प.6.1.142"


class Sutra61142:
	def apply(self, word, pos):
		return apply_6_1_142(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.142:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.142:marker=padartha;input=रामः'),
		('सीता', '', '6.1.142:marker=padartha;input=सीता'),
	]
