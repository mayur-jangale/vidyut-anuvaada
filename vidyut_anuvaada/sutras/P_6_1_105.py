# Sutra प.6.1.105: दीर्घाज्जसि च
# sandhi-sūtra प.6.1.105

from P_6_1 import apply_6_1_105

SUTRA_CODE = "प.6.1.105"
SUTRA_TEXT = "दीर्घाज्जसि च"
SUTRA_DESC = "sandhi-sūtra प.6.1.105"


class Sutra61105:
	def apply(self, word, pos):
		return apply_6_1_105(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.105:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.105:marker=padartha;input=रामः'),
		('सीता', '', '6.1.105:marker=padartha;input=सीता'),
	]
