# Sutra प.6.1.60: शीर्षंश्छन्दसि
# sandhi-sūtra प.6.1.60

from P_6_1 import apply_6_1_60

SUTRA_CODE = "प.6.1.60"
SUTRA_TEXT = "शीर्षंश्छन्दसि"
SUTRA_DESC = "sandhi-sūtra प.6.1.60"


class Sutra6160:
	def apply(self, word, pos):
		return apply_6_1_60(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.60:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.60:marker=padartha;input=रामः'),
		('सीता', '', '6.1.60:marker=padartha;input=सीता'),
	]
