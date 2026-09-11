# Sutra प.6.1.34: बहुलं छन्दसि
# sandhi-sūtra प.6.1.34

from P_6_1 import apply_6_1_34

SUTRA_CODE = "प.6.1.34"
SUTRA_TEXT = "बहुलं छन्दसि"
SUTRA_DESC = "sandhi-sūtra प.6.1.34"


class Sutra6134:
	def apply(self, word, pos):
		return apply_6_1_34(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.34:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.34:marker=padartha;input=रामः'),
		('सीता', '', '6.1.34:marker=padartha;input=सीता'),
	]
