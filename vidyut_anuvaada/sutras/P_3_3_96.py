# Sutra प.3.3.96: मन्त्रे वृषेषपचमनविदभूवीरा उदात्तः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — mantre vfzezapacamanavidaBUvIrA udAttaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.96"
SUTRA_TEXT = "मन्त्रे वृषेषपचमनविदभूवीरा उदात्तः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — mantre vfzezapacamanavidaBUvIrA udAttaH"


class Sutra3396:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

