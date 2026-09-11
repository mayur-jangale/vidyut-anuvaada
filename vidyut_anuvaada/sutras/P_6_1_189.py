# Sutra प.6.1.189: अभ्यस्तानामादिः
# sandhi-sūtra प.6.1.189

from P_6_1 import apply_6_1_189

SUTRA_CODE = "प.6.1.189"
SUTRA_TEXT = "अभ्यस्तानामादिः"
SUTRA_DESC = "sandhi-sūtra प.6.1.189"


class Sutra61189:
	def apply(self, word, pos):
		return apply_6_1_189(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.189:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.189:marker=padartha;input=रामः'),
		('सीता', '', '6.1.189:marker=padartha;input=सीता'),
	]
