# Sutra प.6.4.120: अत एकहल्मध्येऽनादेशादेर्लिटि
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.120"
SUTRA_TEXT = "अत एकहल्मध्येऽनादेशादेर्लिटि"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra64120:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.120: अग्निः'),
		('रामः', '', 'प.6.4.120: रामः'),
		('सीता', '', 'प.6.4.120: सीता'),
	]

