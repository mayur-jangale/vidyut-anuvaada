# Sutra प.6.1.211: युष्मदस्मदोर्ङसि
# sandhi-sūtra प.6.1.211

from P_6_1 import apply_6_1_211

SUTRA_CODE = "प.6.1.211"
SUTRA_TEXT = "युष्मदस्मदोर्ङसि"
SUTRA_DESC = "sandhi-sūtra प.6.1.211"


class Sutra61211:
	def apply(self, word, pos):
		return apply_6_1_211(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.211:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.211:marker=padartha;input=रामः'),
		('सीता', '', '6.1.211:marker=padartha;input=सीता'),
	]
