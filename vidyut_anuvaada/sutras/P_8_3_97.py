# Sutra प.8.3.97: अम्बाम्बगोभूमिसव्यापद्वित्रिकुशेकुशङ्क्वङ्गुमञ्जिपुञ्जिपरमेबर्हिर्दिव्यग्निभ्यः स्थः
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.97"
SUTRA_TEXT = "अम्बाम्बगोभूमिसव्यापद्वित्रिकुशेकुशङ्क्वङ्गुमञ्जिपुञ्जिपरमेबर्हिर्दिव्यग्निभ्यः स्थः"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8397:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.97: अग्निः'),
		('रामः', '', 'प.8.3.97: रामः'),
		('सीता', '', 'प.8.3.97: सीता'),
	]

