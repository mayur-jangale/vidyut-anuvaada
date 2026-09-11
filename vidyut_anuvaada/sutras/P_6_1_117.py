# Sutra प.6.1.117: यजुष्युरः
# sandhi-sūtra प.6.1.117

from P_6_1 import apply_6_1_117

SUTRA_CODE = "प.6.1.117"
SUTRA_TEXT = "यजुष्युरः"
SUTRA_DESC = "sandhi-sūtra प.6.1.117"


class Sutra61117:
	def apply(self, word, pos):
		return apply_6_1_117(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.117:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.117:marker=padartha;input=रामः'),
		('सीता', '', '6.1.117:marker=padartha;input=सीता'),
	]
