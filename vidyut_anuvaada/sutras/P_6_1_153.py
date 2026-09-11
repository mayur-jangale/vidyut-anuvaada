# Sutra प.6.1.153: प्रस्कण्वहरिश्चन्द्रावृषी
# sandhi-sūtra प.6.1.153

from P_6_1 import apply_6_1_153

SUTRA_CODE = "प.6.1.153"
SUTRA_TEXT = "प्रस्कण्वहरिश्चन्द्रावृषी"
SUTRA_DESC = "sandhi-sūtra प.6.1.153"


class Sutra61153:
	def apply(self, word, pos):
		return apply_6_1_153(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.153:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.153:marker=padartha;input=रामः'),
		('सीता', '', '6.1.153:marker=padartha;input=सीता'),
	]
