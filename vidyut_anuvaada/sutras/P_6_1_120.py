# Sutra प.6.1.120: अनुदात्ते च कुधपरे
# sandhi-sūtra प.6.1.120

from P_6_1 import apply_6_1_120

SUTRA_CODE = "प.6.1.120"
SUTRA_TEXT = "अनुदात्ते च कुधपरे"
SUTRA_DESC = "sandhi-sūtra प.6.1.120"


class Sutra61120:
	def apply(self, word, pos):
		return apply_6_1_120(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.120:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.120:marker=padartha;input=रामः'),
		('सीता', '', '6.1.120:marker=padartha;input=सीता'),
	]
