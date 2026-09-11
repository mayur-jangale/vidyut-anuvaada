# Sutra प.6.1.160: उञ्छादीनां च
# sandhi-sūtra प.6.1.160

from P_6_1 import apply_6_1_160

SUTRA_CODE = "प.6.1.160"
SUTRA_TEXT = "उञ्छादीनां च"
SUTRA_DESC = "sandhi-sūtra प.6.1.160"


class Sutra61160:
	def apply(self, word, pos):
		return apply_6_1_160(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.160:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.160:marker=padartha;input=रामः'),
		('सीता', '', '6.1.160:marker=padartha;input=सीता'),
	]
