# Sutra प.3.3.27: प्रे द्रुस्तुस्रुवः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — pre drustusruvaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.27"
SUTRA_TEXT = "प्रे द्रुस्तुस्रुवः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — pre drustusruvaH"


class Sutra3327:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

