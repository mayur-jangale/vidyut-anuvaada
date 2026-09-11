# Sutra प.3.4.21: समानकर्तृकयोः पूर्वकाले
# lyap — absolutive (gerund) suffix

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.21"
SUTRA_TEXT = "समानकर्तृकयोः पूर्वकाले"
SUTRA_DESC = "lyap — absolutive (gerund) suffix"


class Sutra3421:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

