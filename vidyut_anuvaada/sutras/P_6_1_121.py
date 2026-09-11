# Sutra प.6.1.121: अवपथासि च
# sandhi-sūtra प.6.1.121

from P_6_1 import apply_6_1_121

SUTRA_CODE = "प.6.1.121"
SUTRA_TEXT = "अवपथासि च"
SUTRA_DESC = "sandhi-sūtra प.6.1.121"


class Sutra61121:
	def apply(self, word, pos):
		return apply_6_1_121(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.121:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.121:marker=padartha;input=रामः'),
		('सीता', '', '6.1.121:marker=padartha;input=सीता'),
	]
