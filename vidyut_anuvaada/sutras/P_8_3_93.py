# Sutra प.8.3.93: वृक्षासनयोर्विष्टरः
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.93"
SUTRA_TEXT = "वृक्षासनयोर्विष्टरः"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8393:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.93: अग्निः'),
		('रामः', '', 'प.8.3.93: रामः'),
		('सीता', '', 'प.8.3.93: सीता'),
	]

