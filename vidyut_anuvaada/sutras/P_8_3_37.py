# Sutra प.8.3.37: कुप्वोः ≍क≍पौ च
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.37"
SUTRA_TEXT = "कुप्वोः ≍क≍पौ च"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8337:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.37: अग्निः'),
		('रामः', '', 'प.8.3.37: रामः'),
		('सीता', '', 'प.8.3.37: सीता'),
	]

