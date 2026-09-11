# Sutra प.8.3.43: द्विस्त्रिश्चतुरिति कृत्वोऽर्थे
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.43"
SUTRA_TEXT = "द्विस्त्रिश्चतुरिति कृत्वोऽर्थे"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8343:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.43: अग्निः'),
		('रामः', '', 'प.8.3.43: रामः'),
		('सीता', '', 'प.8.3.43: सीता'),
	]

