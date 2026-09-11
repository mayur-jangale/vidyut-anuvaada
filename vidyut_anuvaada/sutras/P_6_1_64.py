# Sutra प.6.1.64: धात्वादेः षः सः
# sandhi-sūtra प.6.1.64

from P_6_1 import apply_6_1_64

SUTRA_CODE = "प.6.1.64"
SUTRA_TEXT = "धात्वादेः षः सः"
SUTRA_DESC = "sandhi-sūtra प.6.1.64"


class Sutra6164:
	def apply(self, word, pos):
		return apply_6_1_64(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.64:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.64:marker=padartha;input=रामः'),
		('सीता', '', '6.1.64:marker=padartha;input=सीता'),
	]
