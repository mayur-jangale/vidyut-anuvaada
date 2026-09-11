# Sutra प.6.1.85: अन्तादिवच्च
# sandhi-sūtra प.6.1.85

from P_6_1 import apply_6_1_85

SUTRA_CODE = "प.6.1.85"
SUTRA_TEXT = "अन्तादिवच्च"
SUTRA_DESC = "sandhi-sūtra प.6.1.85"


class Sutra6185:
	def apply(self, word, pos):
		return apply_6_1_85(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.85:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.85:marker=padartha;input=रामः'),
		('सीता', '', '6.1.85:marker=padartha;input=सीता'),
	]
