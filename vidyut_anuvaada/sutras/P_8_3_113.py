# Sutra प.8.3.113: सेधतेर्गतौ
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.113"
SUTRA_TEXT = "सेधतेर्गतौ"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra83113:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.113: अग्निः'),
		('रामः', '', 'प.8.3.113: रामः'),
		('सीता', '', 'प.8.3.113: सीता'),
	]

