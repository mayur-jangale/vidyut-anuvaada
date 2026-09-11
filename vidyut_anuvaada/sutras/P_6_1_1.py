# Sutra प.6.1.1: एकाचो द्वे प्रथमस्य
# sandhi-sūtra प.6.1.1

from P_6_1 import apply_6_1_1

SUTRA_CODE = "प.6.1.1"
SUTRA_TEXT = "एकाचो द्वे प्रथमस्य"
SUTRA_DESC = "sandhi-sūtra प.6.1.1"


class Sutra611:
	def apply(self, word, pos):
		return apply_6_1_1(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.1:input=अग्निः'),
		('रामः', '', '6.1.1:input=रामः'),
		('सीता', '', '6.1.1:input=सीता'),
	]
