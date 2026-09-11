# Sutra प.6.1.68: हल्ङ्याब्भ्यो दीर्घात् सुतिस्यपृक्तं हल्
# sandhi-sūtra प.6.1.68

from P_6_1 import apply_6_1_68

SUTRA_CODE = "प.6.1.68"
SUTRA_TEXT = "हल्ङ्याब्भ्यो दीर्घात् सुतिस्यपृक्तं हल्"
SUTRA_DESC = "sandhi-sūtra प.6.1.68"


class Sutra6168:
	def apply(self, word, pos):
		return apply_6_1_68(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.68:input=अग्निः'),
		('रामः', '', '6.1.68:input=रामः'),
		('सीता', '', '6.1.68:input=सीता'),
	]
