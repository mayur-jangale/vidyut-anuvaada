# Sutra प.6.1.195: अचः कर्तृयकि
# sandhi-sūtra प.6.1.195

from P_6_1 import apply_6_1_195

SUTRA_CODE = "प.6.1.195"
SUTRA_TEXT = "अचः कर्तृयकि"
SUTRA_DESC = "sandhi-sūtra प.6.1.195"


class Sutra61195:
	def apply(self, word, pos):
		return apply_6_1_195(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.195:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.195:marker=padartha;input=रामः'),
		('सीता', '', '6.1.195:marker=padartha;input=सीता'),
	]
