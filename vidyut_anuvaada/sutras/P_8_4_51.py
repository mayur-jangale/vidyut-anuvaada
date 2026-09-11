# Sutra प.8.4.51: सर्वत्र शाकल्यस्य
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.51"
SUTRA_TEXT = "सर्वत्र शाकल्यस्य"
SUTRA_DESC = "final transformations — continued"


class Sutra8451:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.51: अग्निः'),
		('रामः', '', 'प.8.4.51: रामः'),
		('सीता', '', 'प.8.4.51: सीता'),
	]

