# Sutra प.6.1.107: अमि पूर्वः
# sandhi-sūtra प.6.1.107

from P_6_1 import apply_6_1_107

SUTRA_CODE = "प.6.1.107"
SUTRA_TEXT = "अमि पूर्वः"
SUTRA_DESC = "sandhi-sūtra प.6.1.107"


class Sutra61107:
	def apply(self, word, pos):
		return apply_6_1_107(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.107:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.107:marker=padartha;input=रामः'),
		('सीता', '', '6.1.107:marker=padartha;input=सीता'),
	]
