# Sutra प.6.4.1: अङ्गस्य
# samprasāraṇa — vowel transformation rules

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.1"
SUTRA_TEXT = "अङ्गस्य"
SUTRA_DESC = "samprasāraṇa — vowel transformation rules"


class Sutra641:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.1: अग्निः'),
		('रामः', '', 'प.6.4.1: रामः'),
		('सीता', '', 'प.6.4.1: सीता'),
	]

