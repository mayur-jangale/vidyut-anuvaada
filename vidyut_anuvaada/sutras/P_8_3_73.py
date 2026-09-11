# Sutra प.8.3.73: वेः स्कन्देरनिष्ठायाम्
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.73"
SUTRA_TEXT = "वेः स्कन्देरनिष्ठायाम्"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8373:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.73: अग्निः'),
		('रामः', '', 'प.8.3.73: रामः'),
		('सीता', '', 'प.8.3.73: सीता'),
	]

