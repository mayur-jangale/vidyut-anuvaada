# Sutra प.2.2.24: अनेकमन्यपदार्थे
# (Samasa (compound formation)) — anekamanyapadArTe

from sutra_engines import apply_general

SUTRA_CODE = "प.2.2.24"
SUTRA_TEXT = "अनेकमन्यपदार्थे"
SUTRA_DESC = "(Samasa (compound formation)) — anekamanyapadArTe"


class Sutra2224:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

