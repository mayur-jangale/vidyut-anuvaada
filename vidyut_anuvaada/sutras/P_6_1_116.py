# Sutra प.6.1.116: अव्यादवद्यादवक्रमुरव्रतायमवन्त्ववस्युषु च
# sandhi-sūtra प.6.1.116

from P_6_1 import apply_6_1_116

SUTRA_CODE = "प.6.1.116"
SUTRA_TEXT = "अव्यादवद्यादवक्रमुरव्रतायमवन्त्ववस्युषु च"
SUTRA_DESC = "sandhi-sūtra प.6.1.116"


class Sutra61116:
	def apply(self, word, pos):
		return apply_6_1_116(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.116:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.116:marker=padartha;input=रामः'),
		('सीता', '', '6.1.116:marker=padartha;input=सीता'),
	]
