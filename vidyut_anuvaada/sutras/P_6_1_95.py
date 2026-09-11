# Sutra प.6.1.95: ओमाङोश्च
# sandhi-sūtra प.6.1.95

from P_6_1 import apply_6_1_95

SUTRA_CODE = "प.6.1.95"
SUTRA_TEXT = "ओमाङोश्च"
SUTRA_DESC = "sandhi-sūtra प.6.1.95"


class Sutra6195:
	def apply(self, word, pos):
		return apply_6_1_95(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.95:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.95:marker=padartha;input=रामः'),
		('सीता', '', '6.1.95:marker=padartha;input=सीता'),
	]
