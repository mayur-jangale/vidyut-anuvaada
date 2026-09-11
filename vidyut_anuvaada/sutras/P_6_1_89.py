# Sutra प.6.1.89: एत्येधत्यूठ्सु
# sandhi-sūtra प.6.1.89

from P_6_1 import apply_6_1_89

SUTRA_CODE = "प.6.1.89"
SUTRA_TEXT = "एत्येधत्यूठ्सु"
SUTRA_DESC = "sandhi-sūtra प.6.1.89"


class Sutra6189:
	def apply(self, word, pos):
		return apply_6_1_89(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.89:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.89:marker=padartha;input=रामः'),
		('सीता', '', '6.1.89:marker=padartha;input=सीता'),
	]
