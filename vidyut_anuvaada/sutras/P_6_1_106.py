# Sutra प.6.1.106: वा छन्दसि
# sandhi-sūtra प.6.1.106

from P_6_1 import apply_6_1_106

SUTRA_CODE = "प.6.1.106"
SUTRA_TEXT = "वा छन्दसि"
SUTRA_DESC = "sandhi-sūtra प.6.1.106"


class Sutra61106:
	def apply(self, word, pos):
		return apply_6_1_106(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.106:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.106:marker=padartha;input=रामः'),
		('सीता', '', '6.1.106:marker=padartha;input=सीता'),
	]
