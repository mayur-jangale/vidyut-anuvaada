# Sutra प.6.1.103: तस्माच्छसो नः पुंसि
# sandhi-sūtra प.6.1.103

from P_6_1 import apply_6_1_103

SUTRA_CODE = "प.6.1.103"
SUTRA_TEXT = "तस्माच्छसो नः पुंसि"
SUTRA_DESC = "sandhi-sūtra प.6.1.103"


class Sutra61103:
	def apply(self, word, pos):
		return apply_6_1_103(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.103:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.103:marker=padartha;input=रामः'),
		('सीता', '', '6.1.103:marker=padartha;input=सीता'),
	]
