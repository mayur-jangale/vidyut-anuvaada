# Sutra प.6.1.47: स्फुरतिस्फुलत्योर्घञि
# sandhi-sūtra प.6.1.47

from P_6_1 import apply_6_1_47

SUTRA_CODE = "प.6.1.47"
SUTRA_TEXT = "स्फुरतिस्फुलत्योर्घञि"
SUTRA_DESC = "sandhi-sūtra प.6.1.47"


class Sutra6147:
	def apply(self, word, pos):
		return apply_6_1_47(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.47:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.47:marker=padartha;input=रामः'),
		('सीता', '', '6.1.47:marker=padartha;input=सीता'),
	]
