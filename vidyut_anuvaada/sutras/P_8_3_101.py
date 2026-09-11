# Sutra प.8.3.101: ह्रस्वात् तादौ तद्धिते
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.101"
SUTRA_TEXT = "ह्रस्वात् तादौ तद्धिते"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra83101:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.101: अग्निः'),
		('रामः', '', 'प.8.3.101: रामः'),
		('सीता', '', 'प.8.3.101: सीता'),
	]

