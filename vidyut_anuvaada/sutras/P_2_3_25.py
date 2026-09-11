# Sutra प.2.3.25: विभाषा गुणेऽस्त्रियाम्
# (Samasa (compound formation)) — viBAzA guRe'striyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.25"
SUTRA_TEXT = "विभाषा गुणेऽस्त्रियाम्"
SUTRA_DESC = "(Samasa (compound formation)) — viBAzA guRe'striyAm"


class Sutra2325:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

