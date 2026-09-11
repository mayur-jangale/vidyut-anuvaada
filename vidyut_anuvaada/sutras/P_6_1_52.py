# Sutra प.6.1.52: खिदेश्छन्दसि
# sandhi-sūtra प.6.1.52

from P_6_1 import apply_6_1_52

SUTRA_CODE = "प.6.1.52"
SUTRA_TEXT = "खिदेश्छन्दसि"
SUTRA_DESC = "sandhi-sūtra प.6.1.52"


class Sutra6152:
	def apply(self, word, pos):
		return apply_6_1_52(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.52:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.52:marker=padartha;input=रामः'),
		('सीता', '', '6.1.52:marker=padartha;input=सीता'),
	]
