# Sutra प.6.1.127: इकोऽसवर्णे शाकल्यस्य ह्रस्वश्च
# sandhi-sūtra प.6.1.127

from P_6_1 import apply_6_1_127

SUTRA_CODE = "प.6.1.127"
SUTRA_TEXT = "इकोऽसवर्णे शाकल्यस्य ह्रस्वश्च"
SUTRA_DESC = "sandhi-sūtra प.6.1.127"


class Sutra61127:
	def apply(self, word, pos):
		return apply_6_1_127(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.127:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.127:marker=padartha;input=रामः'),
		('सीता', '', '6.1.127:marker=padartha;input=सीता'),
	]
