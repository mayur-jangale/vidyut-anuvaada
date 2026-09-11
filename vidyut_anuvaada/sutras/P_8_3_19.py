# Sutra प.8.3.19: लोपः शाकल्यस्य
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.19"
SUTRA_TEXT = "लोपः शाकल्यस्य"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8319:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.19: अग्निः'),
		('रामः', '', 'प.8.3.19: रामः'),
		('सीता', '', 'प.8.3.19: सीता'),
	]

