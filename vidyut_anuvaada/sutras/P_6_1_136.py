# Sutra प.6.1.136: अडभ्यासव्यवायेऽपि
# sandhi-sūtra प.6.1.136

from P_6_1 import apply_6_1_136

SUTRA_CODE = "प.6.1.136"
SUTRA_TEXT = "अडभ्यासव्यवायेऽपि"
SUTRA_DESC = "sandhi-sūtra प.6.1.136"


class Sutra61136:
	def apply(self, word, pos):
		return apply_6_1_136(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.136:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.136:marker=padartha;input=रामः'),
		('सीता', '', '6.1.136:marker=padartha;input=सीता'),
	]
