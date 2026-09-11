# Sutra प.6.1.39: वश्चास्यान्यतरस्याम् किति
# sandhi-sūtra प.6.1.39

from P_6_1 import apply_6_1_39

SUTRA_CODE = "प.6.1.39"
SUTRA_TEXT = "वश्चास्यान्यतरस्याम् किति"
SUTRA_DESC = "sandhi-sūtra प.6.1.39"


class Sutra6139:
	def apply(self, word, pos):
		return apply_6_1_39(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.39:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.39:marker=padartha;input=रामः'),
		('सीता', '', '6.1.39:marker=padartha;input=सीता'),
	]
