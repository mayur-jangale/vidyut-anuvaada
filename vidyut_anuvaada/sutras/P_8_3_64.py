# Sutra प.8.3.64: स्थाऽऽदिष्वभ्यासेन चाभ्यासस्य
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.64"
SUTRA_TEXT = "स्थाऽऽदिष्वभ्यासेन चाभ्यासस्य"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8364:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.64: अग्निः'),
		('रामः', '', 'प.8.3.64: रामः'),
		('सीता', '', 'प.8.3.64: सीता'),
	]

