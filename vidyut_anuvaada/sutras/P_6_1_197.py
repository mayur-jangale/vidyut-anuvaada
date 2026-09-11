# Sutra प.6.1.197: ञ्नित्यादिर्नित्यम्
# sandhi-sūtra प.6.1.197

from P_6_1 import apply_6_1_197

SUTRA_CODE = "प.6.1.197"
SUTRA_TEXT = "ञ्नित्यादिर्नित्यम्"
SUTRA_DESC = "sandhi-sūtra प.6.1.197"


class Sutra61197:
	def apply(self, word, pos):
		return apply_6_1_197(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.197:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.197:marker=padartha;input=रामः'),
		('सीता', '', '6.1.197:marker=padartha;input=सीता'),
	]
