# Sutra प.8.3.75: परिस्कन्दः प्राच्यभरतेषु
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.75"
SUTRA_TEXT = "परिस्कन्दः प्राच्यभरतेषु"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8375:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.75: अग्निः'),
		('रामः', '', 'प.8.3.75: रामः'),
		('सीता', '', 'प.8.3.75: सीता'),
	]

