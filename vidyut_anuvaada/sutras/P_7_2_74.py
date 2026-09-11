# Sutra प.7.2.74: स्मिपूङ्रञ्ज्वशां सनि
# (Taddhita (secondary derivations)) — smipUNraYjvaSAM sani

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.74"
SUTRA_TEXT = "स्मिपूङ्रञ्ज्वशां सनि"
SUTRA_DESC = "(Taddhita (secondary derivations)) — smipUNraYjvaSAM sani"


class Sutra7274:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.74: अग्निः'),
		('रामः', '', 'प.7.2.74: रामः'),
		('सीता', '', 'प.7.2.74: सीता'),
	]

