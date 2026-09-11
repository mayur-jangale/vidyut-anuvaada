# Sutra प.6.1.83: भय्यप्रवय्ये च च्छन्दसि
# sandhi-sūtra प.6.1.83

from P_6_1 import apply_6_1_83

SUTRA_CODE = "प.6.1.83"
SUTRA_TEXT = "भय्यप्रवय्ये च च्छन्दसि"
SUTRA_DESC = "sandhi-sūtra प.6.1.83"


class Sutra6183:
	def apply(self, word, pos):
		return apply_6_1_83(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.83:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.83:marker=padartha;input=रामः'),
		('सीता', '', '6.1.83:marker=padartha;input=सीता'),
	]
