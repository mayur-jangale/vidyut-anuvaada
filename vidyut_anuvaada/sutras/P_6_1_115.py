# Sutra प.6.1.115: प्रकृत्याऽन्तःपादमव्यपरे
# sandhi-sūtra प.6.1.115

from P_6_1 import apply_6_1_115

SUTRA_CODE = "प.6.1.115"
SUTRA_TEXT = "प्रकृत्याऽन्तःपादमव्यपरे"
SUTRA_DESC = "sandhi-sūtra प.6.1.115"


class Sutra61115:
	def apply(self, word, pos):
		return apply_6_1_115(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.115:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.115:marker=padartha;input=रामः'),
		('सीता', '', '6.1.115:marker=padartha;input=सीता'),
	]
