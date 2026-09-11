# Sutra प.6.1.188: स्वपादिहिंसामच्यनिटि
# sandhi-sūtra प.6.1.188

from P_6_1 import apply_6_1_188

SUTRA_CODE = "प.6.1.188"
SUTRA_TEXT = "स्वपादिहिंसामच्यनिटि"
SUTRA_DESC = "sandhi-sūtra प.6.1.188"


class Sutra61188:
	def apply(self, word, pos):
		return apply_6_1_188(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.188:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.188:marker=padartha;input=रामः'),
		('सीता', '', '6.1.188:marker=padartha;input=सीता'),
	]
