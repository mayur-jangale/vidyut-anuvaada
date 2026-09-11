# Sutra प.6.1.199: पथिमथोः सर्वनामस्थाने
# sandhi-sūtra प.6.1.199

from P_6_1 import apply_6_1_199

SUTRA_CODE = "प.6.1.199"
SUTRA_TEXT = "पथिमथोः सर्वनामस्थाने"
SUTRA_DESC = "sandhi-sūtra प.6.1.199"


class Sutra61199:
	def apply(self, word, pos):
		return apply_6_1_199(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.199:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.199:marker=padartha;input=रामः'),
		('सीता', '', '6.1.199:marker=padartha;input=सीता'),
	]
