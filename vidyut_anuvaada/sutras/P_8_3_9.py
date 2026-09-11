# Sutra प.8.3.9: दीर्घादटि समानपादे
# aṅgasya — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.9"
SUTRA_TEXT = "दीर्घादटि समानपादे"
SUTRA_DESC = "aṅgasya — repeated"


class Sutra839:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.9: अग्निः'),
		('रामः', '', 'प.8.3.9: रामः'),
		('सीता', '', 'प.8.3.9: सीता'),
	]

