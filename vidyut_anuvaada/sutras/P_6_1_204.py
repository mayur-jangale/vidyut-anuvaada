# Sutra प.6.1.204: संज्ञायामुपमानम्
# sandhi-sūtra प.6.1.204

from P_6_1 import apply_6_1_204

SUTRA_CODE = "प.6.1.204"
SUTRA_TEXT = "संज्ञायामुपमानम्"
SUTRA_DESC = "sandhi-sūtra प.6.1.204"


class Sutra61204:
	def apply(self, word, pos):
		return apply_6_1_204(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.204:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.204:marker=padartha;input=रामः'),
		('सीता', '', '6.1.204:marker=padartha;input=सीता'),
	]
