# Sutra प.5.2.115: अत इनिठनौ
# in — possessive suffix (wealthy)

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.115"
SUTRA_TEXT = "अत इनिठनौ"
SUTRA_DESC = "in — possessive suffix (wealthy)"


class Sutra52115:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.115: अग्निः'),
		('रामः', '', 'प.5.2.115: रामः'),
		('सीता', '', 'प.5.2.115: सीता'),
	]

