# Sutra प.6.1.178: ङ्याश्छन्दसि बहुलम्
# sandhi-sūtra प.6.1.178

from P_6_1 import apply_6_1_178

SUTRA_CODE = "प.6.1.178"
SUTRA_TEXT = "ङ्याश्छन्दसि बहुलम्"
SUTRA_DESC = "sandhi-sūtra प.6.1.178"


class Sutra61178:
	def apply(self, word, pos):
		return apply_6_1_178(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.178:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.178:marker=padartha;input=रामः'),
		('सीता', '', '6.1.178:marker=padartha;input=सीता'),
	]
