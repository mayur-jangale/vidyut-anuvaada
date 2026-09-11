# Sutra प.7.3.120: आङो नाऽस्त्रियाम्
# (Taddhita (secondary derivations)) — ANo nA'striyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.120"
SUTRA_TEXT = "आङो नाऽस्त्रियाम्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — ANo nA'striyAm"


class Sutra73120:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.120: अग्निः'),
		('रामः', '', 'प.7.3.120: रामः'),
		('सीता', '', 'प.7.3.120: सीता'),
	]

