# Sutra प.6.1.70: शेश्छन्दसि बहुलम्
# sandhi-sūtra प.6.1.70

from P_6_1 import apply_6_1_70

SUTRA_CODE = "प.6.1.70"
SUTRA_TEXT = "शेश्छन्दसि बहुलम्"
SUTRA_DESC = "sandhi-sūtra प.6.1.70"


class Sutra6170:
	def apply(self, word, pos):
		return apply_6_1_70(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.70:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.70:marker=padartha;input=रामः'),
		('सीता', '', '6.1.70:marker=padartha;input=सीता'),
	]
