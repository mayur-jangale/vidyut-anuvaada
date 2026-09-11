# Sutra प.3.2.102: निष्ठा
# kta — past passive participle (PPP) suffix

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.102"
SUTRA_TEXT = "निष्ठा"
SUTRA_DESC = "kta — past passive participle (PPP) suffix"


class Sutra32102:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

