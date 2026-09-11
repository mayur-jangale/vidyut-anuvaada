# Sutra प.6.3.66: खित्यनव्ययस्य
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.66"
SUTRA_TEXT = "खित्यनव्ययस्य"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6366:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.66: अग्निः'),
		('रामः', '', 'प.6.3.66: रामः'),
		('सीता', '', 'प.6.3.66: सीता'),
	]

