# Sutra प.8.3.35: शर्परे विसर्जनीयः
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.35"
SUTRA_TEXT = "शर्परे विसर्जनीयः"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8335:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.35: अग्निः'),
		('रामः', '', 'प.8.3.35: रामः'),
		('सीता', '', 'प.8.3.35: सीता'),
	]

