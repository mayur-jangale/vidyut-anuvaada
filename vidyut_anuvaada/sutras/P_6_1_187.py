# Sutra प.6.1.187: आदिः सिचोऽन्यतरस्याम्
# sandhi-sūtra प.6.1.187

from P_6_1 import apply_6_1_187

SUTRA_CODE = "प.6.1.187"
SUTRA_TEXT = "आदिः सिचोऽन्यतरस्याम्"
SUTRA_DESC = "sandhi-sūtra प.6.1.187"


class Sutra61187:
	def apply(self, word, pos):
		return apply_6_1_187(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.187:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.187:marker=padartha;input=रामः'),
		('सीता', '', '6.1.187:marker=padartha;input=सीता'),
	]
