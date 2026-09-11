# Sutra प.6.1.186: तास्यनुदात्तेन्ङिददुपदेशाल्लसार्वधातुकमनुदात्तमह्न्विङोः
# sandhi-sūtra प.6.1.186

from P_6_1 import apply_6_1_186

SUTRA_CODE = "प.6.1.186"
SUTRA_TEXT = "तास्यनुदात्तेन्ङिददुपदेशाल्लसार्वधातुकमनुदात्तमह्न्विङोः"
SUTRA_DESC = "sandhi-sūtra प.6.1.186"


class Sutra61186:
	def apply(self, word, pos):
		return apply_6_1_186(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.186:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.186:marker=padartha;input=रामः'),
		('सीता', '', '6.1.186:marker=padartha;input=सीता'),
	]
