# Sutra प.6.1.182: न गोश्वन्त्साववर्णराडङ्क्रुङ्कृद्भ्यः
# sandhi-sūtra प.6.1.182

from P_6_1 import apply_6_1_182

SUTRA_CODE = "प.6.1.182"
SUTRA_TEXT = "न गोश्वन्त्साववर्णराडङ्क्रुङ्कृद्भ्यः"
SUTRA_DESC = "sandhi-sūtra प.6.1.182"


class Sutra61182:
	def apply(self, word, pos):
		return apply_6_1_182(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.182:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.182:marker=padartha;input=रामः'),
		('सीता', '', '6.1.182:marker=padartha;input=सीता'),
	]
