# Sutra प.6.1.218: चङ्यन्यतरस्याम्
# sandhi-sūtra प.6.1.218

from P_6_1 import apply_6_1_218

SUTRA_CODE = "प.6.1.218"
SUTRA_TEXT = "चङ्यन्यतरस्याम्"
SUTRA_DESC = "sandhi-sūtra प.6.1.218"


class Sutra61218:
	def apply(self, word, pos):
		return apply_6_1_218(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.218:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.218:marker=padartha;input=रामः'),
		('सीता', '', '6.1.218:marker=padartha;input=सीता'),
	]
