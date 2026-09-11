# Sutra प.6.1.4: पूर्वोऽभ्यासः
# sandhi-sūtra प.6.1.4

from P_6_1 import apply_6_1_4

SUTRA_CODE = "प.6.1.4"
SUTRA_TEXT = "पूर्वोऽभ्यासः"
SUTRA_DESC = "sandhi-sūtra प.6.1.4"


class Sutra614:
	def apply(self, word, pos):
		return apply_6_1_4(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.4:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.4:marker=padartha;input=रामः'),
		('सीता', '', '6.1.4:marker=padartha;input=सीता'),
	]
