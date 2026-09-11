# Sutra प.6.1.29: लिड्यङोश्च
# sandhi-sūtra प.6.1.29

from P_6_1 import apply_6_1_29

SUTRA_CODE = "प.6.1.29"
SUTRA_TEXT = "लिड्यङोश्च"
SUTRA_DESC = "sandhi-sūtra प.6.1.29"


class Sutra6129:
	def apply(self, word, pos):
		return apply_6_1_29(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.29:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.29:marker=padartha;input=रामः'),
		('सीता', '', '6.1.29:marker=padartha;input=सीता'),
	]
