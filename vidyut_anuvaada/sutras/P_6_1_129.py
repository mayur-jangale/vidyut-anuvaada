# Sutra प.6.1.129: अप्लुतवदुपस्थिते
# sandhi-sūtra प.6.1.129

from P_6_1 import apply_6_1_129

SUTRA_CODE = "प.6.1.129"
SUTRA_TEXT = "अप्लुतवदुपस्थिते"
SUTRA_DESC = "sandhi-sūtra प.6.1.129"


class Sutra61129:
	def apply(self, word, pos):
		return apply_6_1_129(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.129:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.129:marker=padartha;input=रामः'),
		('सीता', '', '6.1.129:marker=padartha;input=सीता'),
	]
