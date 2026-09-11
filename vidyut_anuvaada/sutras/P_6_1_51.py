# Sutra प.6.1.51: विभाषा लीयतेः
# sandhi-sūtra प.6.1.51

from P_6_1 import apply_6_1_51

SUTRA_CODE = "प.6.1.51"
SUTRA_TEXT = "विभाषा लीयतेः"
SUTRA_DESC = "sandhi-sūtra प.6.1.51"


class Sutra6151:
	def apply(self, word, pos):
		return apply_6_1_51(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.51:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.51:marker=padartha;input=रामः'),
		('सीता', '', '6.1.51:marker=padartha;input=सीता'),
	]
