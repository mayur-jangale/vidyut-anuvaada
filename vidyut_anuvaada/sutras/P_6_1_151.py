# Sutra प.6.1.151: ह्रस्वाच्चन्द्रोत्तरपदे मन्त्रे
# sandhi-sūtra प.6.1.151

from P_6_1 import apply_6_1_151

SUTRA_CODE = "प.6.1.151"
SUTRA_TEXT = "ह्रस्वाच्चन्द्रोत्तरपदे मन्त्रे"
SUTRA_DESC = "sandhi-sūtra प.6.1.151"


class Sutra61151:
	def apply(self, word, pos):
		return apply_6_1_151(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.151:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.151:marker=padartha;input=रामः'),
		('सीता', '', '6.1.151:marker=padartha;input=सीता'),
	]
