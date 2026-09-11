# Sutra प.6.1.209: जुष्टार्पिते च छन्दसि
# sandhi-sūtra प.6.1.209

from P_6_1 import apply_6_1_209

SUTRA_CODE = "प.6.1.209"
SUTRA_TEXT = "जुष्टार्पिते च छन्दसि"
SUTRA_DESC = "sandhi-sūtra प.6.1.209"


class Sutra61209:
	def apply(self, word, pos):
		return apply_6_1_209(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.209:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.209:marker=padartha;input=रामः'),
		('सीता', '', '6.1.209:marker=padartha;input=सीता'),
	]
