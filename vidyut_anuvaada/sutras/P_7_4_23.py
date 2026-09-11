# Sutra प.7.4.23: उपसर्गाद्ध्रस्व ऊहतेः
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.23"
SUTRA_TEXT = "उपसर्गाद्ध्रस्व ऊहतेः"
SUTRA_DESC = "taddhita — continued"


class Sutra7423:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.23: अग्निः'),
		('रामः', '', 'प.7.4.23: रामः'),
		('सीता', '', 'प.7.4.23: सीता'),
	]

