# Sutra प.6.1.38: लिटि वयो यः
# sandhi-sūtra प.6.1.38

from P_6_1 import apply_6_1_38

SUTRA_CODE = "प.6.1.38"
SUTRA_TEXT = "लिटि वयो यः"
SUTRA_DESC = "sandhi-sūtra प.6.1.38"


class Sutra6138:
	def apply(self, word, pos):
		return apply_6_1_38(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.38:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.38:marker=padartha;input=रामः'),
		('सीता', '', '6.1.38:marker=padartha;input=सीता'),
	]
