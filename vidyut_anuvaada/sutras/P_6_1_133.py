# Sutra प.6.1.133: स्यश्छन्दसि बहुलम्
# sandhi-sūtra प.6.1.133

from P_6_1 import apply_6_1_133

SUTRA_CODE = "प.6.1.133"
SUTRA_TEXT = "स्यश्छन्दसि बहुलम्"
SUTRA_DESC = "sandhi-sūtra प.6.1.133"


class Sutra61133:
	def apply(self, word, pos):
		return apply_6_1_133(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.133:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.133:marker=padartha;input=रामः'),
		('सीता', '', '6.1.133:marker=padartha;input=सीता'),
	]
