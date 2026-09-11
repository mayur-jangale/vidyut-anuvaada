# Sutra प.8.3.23: मोऽनुस्वारः
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.23"
SUTRA_TEXT = "मोऽनुस्वारः"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8323:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.23: अग्निः'),
		('रामः', '', 'प.8.3.23: रामः'),
		('सीता', '', 'प.8.3.23: सीता'),
	]

