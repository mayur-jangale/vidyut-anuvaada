# Sutra प.3.2.149: अनुदात्तेतश्च हलादेः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — anudAttetaSca halAdeH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.149"
SUTRA_TEXT = "अनुदात्तेतश्च हलादेः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — anudAttetaSca halAdeH"


class Sutra32149:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

