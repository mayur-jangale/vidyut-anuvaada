# Sutra प.6.1.219: मतोः पूर्वमात् संज्ञायां स्त्रियाम्
# sandhi-sūtra प.6.1.219

from P_6_1 import apply_6_1_219

SUTRA_CODE = "प.6.1.219"
SUTRA_TEXT = "मतोः पूर्वमात् संज्ञायां स्त्रियाम्"
SUTRA_DESC = "sandhi-sūtra प.6.1.219"


class Sutra61219:
	def apply(self, word, pos):
		return apply_6_1_219(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.219:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.219:marker=padartha;input=रामः'),
		('सीता', '', '6.1.219:marker=padartha;input=सीता'),
	]
