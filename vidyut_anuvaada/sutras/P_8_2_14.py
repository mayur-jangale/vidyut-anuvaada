# Sutra प.8.2.14: राजन्वान् सौराज्ये
# aparatvaṃ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.14"
SUTRA_TEXT = "राजन्वान् सौराज्ये"
SUTRA_DESC = "aparatvaṃ — repeated"


class Sutra8214:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.14: अग्निः'),
		('रामः', '', 'प.8.2.14: रामः'),
		('सीता', '', 'प.8.2.14: सीता'),
	]

