# Sutra प.7.1.79: वा नपुंसकस्य
# (Taddhita (secondary derivations)) — vA napuMsakasya

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.79"
SUTRA_TEXT = "वा नपुंसकस्य"
SUTRA_DESC = "(Taddhita (secondary derivations)) — vA napuMsakasya"


class Sutra7179:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.79: अग्निः'),
		('रामः', '', 'प.7.1.79: रामः'),
		('सीता', '', 'प.7.1.79: सीता'),
	]

