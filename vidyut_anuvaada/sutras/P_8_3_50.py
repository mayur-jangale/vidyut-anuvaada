# Sutra प.8.3.50: कःकरत्करतिकृधिकृतेष्वनदितेः
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.50"
SUTRA_TEXT = "कःकरत्करतिकृधिकृतेष्वनदितेः"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8350:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.50: अग्निः'),
		('रामः', '', 'प.8.3.50: रामः'),
		('सीता', '', 'प.8.3.50: सीता'),
	]

