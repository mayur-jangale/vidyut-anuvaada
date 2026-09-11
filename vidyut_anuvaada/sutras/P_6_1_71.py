# Sutra प.6.1.71: ह्रस्वस्य पिति कृति तुक्
# sandhi-sūtra प.6.1.71

from P_6_1 import apply_6_1_71

SUTRA_CODE = "प.6.1.71"
SUTRA_TEXT = "ह्रस्वस्य पिति कृति तुक्"
SUTRA_DESC = "sandhi-sūtra प.6.1.71"


class Sutra6171:
	def apply(self, word, pos):
		return apply_6_1_71(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.71:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.71:marker=padartha;input=रामः'),
		('सीता', '', '6.1.71:marker=padartha;input=सीता'),
	]
