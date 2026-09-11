# Sutra प.6.1.164: तद्धितस्य
# sandhi-sūtra प.6.1.164

from P_6_1 import apply_6_1_164

SUTRA_CODE = "प.6.1.164"
SUTRA_TEXT = "तद्धितस्य"
SUTRA_DESC = "sandhi-sūtra प.6.1.164"


class Sutra61164:
	def apply(self, word, pos):
		return apply_6_1_164(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.164:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.164:marker=padartha;input=रामः'),
		('सीता', '', '6.1.164:marker=padartha;input=सीता'),
	]
