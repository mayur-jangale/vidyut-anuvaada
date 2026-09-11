# Sutra प.7.3.100: अदः सर्वेषाम्
# (Taddhita (secondary derivations)) — adaH sarvezAm

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.100"
SUTRA_TEXT = "अदः सर्वेषाम्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — adaH sarvezAm"


class Sutra73100:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.100: अग्निः'),
		('रामः', '', 'प.7.3.100: रामः'),
		('सीता', '', 'प.7.3.100: सीता'),
	]

