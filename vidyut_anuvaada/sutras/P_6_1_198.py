# Sutra प.6.1.198: आमन्त्रितस्य च
# sandhi-sūtra प.6.1.198

from P_6_1 import apply_6_1_198

SUTRA_CODE = "प.6.1.198"
SUTRA_TEXT = "आमन्त्रितस्य च"
SUTRA_DESC = "sandhi-sūtra प.6.1.198"


class Sutra61198:
	def apply(self, word, pos):
		return apply_6_1_198(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.198:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.198:marker=padartha;input=रामः'),
		('सीता', '', '6.1.198:marker=padartha;input=सीता'),
	]
