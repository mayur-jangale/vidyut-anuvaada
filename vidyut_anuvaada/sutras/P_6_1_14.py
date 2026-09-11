# Sutra प.6.1.14: बन्धुनि बहुव्रीहौ
# sandhi-sūtra प.6.1.14

from P_6_1 import apply_6_1_14

SUTRA_CODE = "प.6.1.14"
SUTRA_TEXT = "बन्धुनि बहुव्रीहौ"
SUTRA_DESC = "sandhi-sūtra प.6.1.14"


class Sutra6114:
	def apply(self, word, pos):
		return apply_6_1_14(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.14:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.14:marker=padartha;input=रामः'),
		('सीता', '', '6.1.14:marker=padartha;input=सीता'),
	]
