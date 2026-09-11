# Sutra प.8.3.95: गवियुधिभ्यां स्थिरः
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.95"
SUTRA_TEXT = "गवियुधिभ्यां स्थिरः"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8395:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.95: अग्निः'),
		('रामः', '', 'प.8.3.95: रामः'),
		('सीता', '', 'प.8.3.95: सीता'),
	]

