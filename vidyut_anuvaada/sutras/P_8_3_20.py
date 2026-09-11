# Sutra प.8.3.20: ओतो गार्ग्यस्य
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.20"
SUTRA_TEXT = "ओतो गार्ग्यस्य"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8320:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.20: अग्निः'),
		('रामः', '', 'प.8.3.20: रामः'),
		('सीता', '', 'प.8.3.20: सीता'),
	]

