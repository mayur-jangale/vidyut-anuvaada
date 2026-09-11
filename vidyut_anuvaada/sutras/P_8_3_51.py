# Sutra प.8.3.51: पञ्चम्याः परावध्यर्थे
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.51"
SUTRA_TEXT = "पञ्चम्याः परावध्यर्थे"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8351:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.51: अग्निः'),
		('रामः', '', 'प.8.3.51: रामः'),
		('सीता', '', 'प.8.3.51: सीता'),
	]

