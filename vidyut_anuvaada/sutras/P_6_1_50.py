# Sutra प.6.1.50: मीनातिमिनोतिदीङां ल्यपि च
# sandhi-sūtra प.6.1.50

from P_6_1 import apply_6_1_50

SUTRA_CODE = "प.6.1.50"
SUTRA_TEXT = "मीनातिमिनोतिदीङां ल्यपि च"
SUTRA_DESC = "sandhi-sūtra प.6.1.50"


class Sutra6150:
	def apply(self, word, pos):
		return apply_6_1_50(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.50:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.50:marker=padartha;input=रामः'),
		('सीता', '', '6.1.50:marker=padartha;input=सीता'),
	]
