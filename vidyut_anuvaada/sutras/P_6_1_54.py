# Sutra प.6.1.54: चिस्फुरोर्णौ
# sandhi-sūtra प.6.1.54

from P_6_1 import apply_6_1_54

SUTRA_CODE = "प.6.1.54"
SUTRA_TEXT = "चिस्फुरोर्णौ"
SUTRA_DESC = "sandhi-sūtra प.6.1.54"


class Sutra6154:
	def apply(self, word, pos):
		return apply_6_1_54(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.54:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.54:marker=padartha;input=रामः'),
		('सीता', '', '6.1.54:marker=padartha;input=सीता'),
	]
