# Sutra प.3.3.26: अवोदोर्नियः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — avodorniyaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.26"
SUTRA_TEXT = "अवोदोर्नियः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — avodorniyaH"


class Sutra3326:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

