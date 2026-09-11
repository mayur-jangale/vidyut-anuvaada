# Sutra प.8.3.38: सोऽपदादौ
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.38"
SUTRA_TEXT = "सोऽपदादौ"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8338:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.38: अग्निः'),
		('रामः', '', 'प.8.3.38: रामः'),
		('सीता', '', 'प.8.3.38: सीता'),
	]

