# Sutra प.5.1.1: प्राक् क्रीताच्छः
# strīpratyaya — feminine suffix rules begin

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.1"
SUTRA_TEXT = "प्राक् क्रीताच्छः"
SUTRA_DESC = "strīpratyaya — feminine suffix rules begin"


class Sutra511:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.1: अग्निः'),
		('रामः', '', 'प.5.1.1: रामः'),
		('सीता', '', 'प.5.1.1: सीता'),
	]

