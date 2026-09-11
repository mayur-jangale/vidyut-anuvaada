# Sutra प.6.1.126: आङोऽनुनासिकश्छन्दसि
# sandhi-sūtra प.6.1.126

from P_6_1 import apply_6_1_126

SUTRA_CODE = "प.6.1.126"
SUTRA_TEXT = "आङोऽनुनासिकश्छन्दसि"
SUTRA_DESC = "sandhi-sūtra प.6.1.126"


class Sutra61126:
	def apply(self, word, pos):
		return apply_6_1_126(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.126:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.126:marker=padartha;input=रामः'),
		('सीता', '', '6.1.126:marker=padartha;input=सीता'),
	]
