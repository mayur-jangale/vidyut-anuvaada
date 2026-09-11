# Sutra प.3.3.25: वौ क्षुश्रुवः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — vO kzuSruvaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.25"
SUTRA_TEXT = "वौ क्षुश्रुवः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — vO kzuSruvaH"


class Sutra3325:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

