# Sutra प.6.1.45: आदेच उपदेशेऽशिति
# sandhi-sūtra प.6.1.45

from P_6_1 import apply_6_1_45

SUTRA_CODE = "प.6.1.45"
SUTRA_TEXT = "आदेच उपदेशेऽशिति"
SUTRA_DESC = "sandhi-sūtra प.6.1.45"


class Sutra6145:
	def apply(self, word, pos):
		return apply_6_1_45(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.45:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.45:marker=padartha;input=रामः'),
		('सीता', '', '6.1.45:marker=padartha;input=सीता'),
	]
