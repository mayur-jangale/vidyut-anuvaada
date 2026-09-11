# Sutra प.3.2.125: सम्बोधने च
# bli — specific PPP formation

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.125"
SUTRA_TEXT = "सम्बोधने च"
SUTRA_DESC = "bli — specific PPP formation"


class Sutra32125:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

