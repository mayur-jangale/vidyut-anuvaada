# Sutra प.3.3.50: विभाषाऽऽङि रुप्लुवोः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — viBAzA''Ni rupluvoH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.50"
SUTRA_TEXT = "विभाषाऽऽङि रुप्लुवोः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — viBAzA''Ni rupluvoH"


class Sutra3350:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

