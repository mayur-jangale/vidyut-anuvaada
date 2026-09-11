# Sutra प.6.3.112: सहिवहोरोदवर्णस्य
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.112"
SUTRA_TEXT = "सहिवहोरोदवर्णस्य"
SUTRA_DESC = "final-sandhi — continued"


class Sutra63112:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.112: अग्निः'),
		('रामः', '', 'प.6.3.112: रामः'),
		('सीता', '', 'प.6.3.112: सीता'),
	]

