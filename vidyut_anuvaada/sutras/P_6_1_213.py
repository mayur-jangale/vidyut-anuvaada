# Sutra प.6.1.213: यतोऽनावः
# sandhi-sūtra प.6.1.213

from P_6_1 import apply_6_1_213

SUTRA_CODE = "प.6.1.213"
SUTRA_TEXT = "यतोऽनावः"
SUTRA_DESC = "sandhi-sūtra प.6.1.213"


class Sutra61213:
	def apply(self, word, pos):
		return apply_6_1_213(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.213:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.213:marker=padartha;input=रामः'),
		('सीता', '', '6.1.213:marker=padartha;input=सीता'),
	]
