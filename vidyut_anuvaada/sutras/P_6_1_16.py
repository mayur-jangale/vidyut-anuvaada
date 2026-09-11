# Sutra प.6.1.16: ग्रहिज्यावयिव्यधिवष्टिविचतिवृश्चतिपृच्छतिभृज्जतीनां ङिति च
# sandhi-sūtra प.6.1.16

from P_6_1 import apply_6_1_16

SUTRA_CODE = "प.6.1.16"
SUTRA_TEXT = "ग्रहिज्यावयिव्यधिवष्टिविचतिवृश्चतिपृच्छतिभृज्जतीनां ङिति च"
SUTRA_DESC = "sandhi-sūtra प.6.1.16"


class Sutra6116:
	def apply(self, word, pos):
		return apply_6_1_16(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.16:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.16:marker=padartha;input=रामः'),
		('सीता', '', '6.1.16:marker=padartha;input=सीता'),
	]
