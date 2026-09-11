# Sutra प.6.1.49: सिध्यतेरपारलौकिके
# sandhi-sūtra प.6.1.49

from P_6_1 import apply_6_1_49

SUTRA_CODE = "प.6.1.49"
SUTRA_TEXT = "सिध्यतेरपारलौकिके"
SUTRA_DESC = "sandhi-sūtra प.6.1.49"


class Sutra6149:
	def apply(self, word, pos):
		return apply_6_1_49(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.49:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.49:marker=padartha;input=रामः'),
		('सीता', '', '6.1.49:marker=padartha;input=सीता'),
	]
