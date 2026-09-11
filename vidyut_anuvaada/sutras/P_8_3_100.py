# Sutra प.8.3.100: नक्षत्राद्वा
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.100"
SUTRA_TEXT = "नक्षत्राद्वा"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra83100:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.100: अग्निः'),
		('रामः', '', 'प.8.3.100: रामः'),
		('सीता', '', 'प.8.3.100: सीता'),
	]

