# Sutra प.6.1.130: ई३ चाक्रवर्मणस्य
# sandhi-sūtra प.6.1.130

from P_6_1 import apply_6_1_130

SUTRA_CODE = "प.6.1.130"
SUTRA_TEXT = "ई३ चाक्रवर्मणस्य"
SUTRA_DESC = "sandhi-sūtra प.6.1.130"


class Sutra61130:
	def apply(self, word, pos):
		return apply_6_1_130(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.130:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.130:marker=padartha;input=रामः'),
		('सीता', '', '6.1.130:marker=padartha;input=सीता'),
	]
