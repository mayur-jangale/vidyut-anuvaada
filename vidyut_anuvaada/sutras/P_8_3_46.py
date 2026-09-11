# Sutra प.8.3.46: अतः कृकमिकंसकुम्भपात्रकुशाकर्णीष्वनव्ययस्य
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.46"
SUTRA_TEXT = "अतः कृकमिकंसकुम्भपात्रकुशाकर्णीष्वनव्ययस्य"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8346:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.46: अग्निः'),
		('रामः', '', 'प.8.3.46: रामः'),
		('सीता', '', 'प.8.3.46: सीता'),
	]

