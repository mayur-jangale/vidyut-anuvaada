# Sutra प.6.1.206: शुष्कधृष्टौ
# sandhi-sūtra प.6.1.206

from P_6_1 import apply_6_1_206

SUTRA_CODE = "प.6.1.206"
SUTRA_TEXT = "शुष्कधृष्टौ"
SUTRA_DESC = "sandhi-sūtra प.6.1.206"


class Sutra61206:
	def apply(self, word, pos):
		return apply_6_1_206(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.206:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.206:marker=padartha;input=रामः'),
		('सीता', '', '6.1.206:marker=padartha;input=सीता'),
	]
