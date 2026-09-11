# Sutra प.8.3.45: नित्यं समासेऽनुत्तरपदस्थस्य
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.45"
SUTRA_TEXT = "नित्यं समासेऽनुत्तरपदस्थस्य"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8345:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.45: अग्निः'),
		('रामः', '', 'प.8.3.45: रामः'),
		('सीता', '', 'प.8.3.45: सीता'),
	]

