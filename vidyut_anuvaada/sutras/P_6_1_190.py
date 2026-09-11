# Sutra प.6.1.190: अनुदात्ते च
# sandhi-sūtra प.6.1.190

from P_6_1 import apply_6_1_190

SUTRA_CODE = "प.6.1.190"
SUTRA_TEXT = "अनुदात्ते च"
SUTRA_DESC = "sandhi-sūtra प.6.1.190"


class Sutra61190:
	def apply(self, word, pos):
		return apply_6_1_190(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.190:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.190:marker=padartha;input=रामः'),
		('सीता', '', '6.1.190:marker=padartha;input=सीता'),
	]
