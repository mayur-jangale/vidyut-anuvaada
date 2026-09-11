# Sutra प.6.1.179: षट्त्रिचतुर्भ्यो हलादिः
# sandhi-sūtra प.6.1.179

from P_6_1 import apply_6_1_179

SUTRA_CODE = "प.6.1.179"
SUTRA_TEXT = "षट्त्रिचतुर्भ्यो हलादिः"
SUTRA_DESC = "sandhi-sūtra प.6.1.179"


class Sutra61179:
	def apply(self, word, pos):
		return apply_6_1_179(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.179:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.179:marker=padartha;input=रामः'),
		('सीता', '', '6.1.179:marker=padartha;input=सीता'),
	]
