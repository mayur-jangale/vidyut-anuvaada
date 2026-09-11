# Sutra प.8.3.103: युष्मत्तत्ततक्षुःष्वन्तःपादम्
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.103"
SUTRA_TEXT = "युष्मत्तत्ततक्षुःष्वन्तःपादम्"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra83103:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.103: अग्निः'),
		('रामः', '', 'प.8.3.103: रामः'),
		('सीता', '', 'प.8.3.103: सीता'),
	]

