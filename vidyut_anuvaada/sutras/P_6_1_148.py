# Sutra प.6.1.148: वर्चस्केऽवस्करः
# sandhi-sūtra प.6.1.148

from P_6_1 import apply_6_1_148

SUTRA_CODE = "प.6.1.148"
SUTRA_TEXT = "वर्चस्केऽवस्करः"
SUTRA_DESC = "sandhi-sūtra प.6.1.148"


class Sutra61148:
	def apply(self, word, pos):
		return apply_6_1_148(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.148:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.148:marker=padartha;input=रामः'),
		('सीता', '', '6.1.148:marker=padartha;input=सीता'),
	]
