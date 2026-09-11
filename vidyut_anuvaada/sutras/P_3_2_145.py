# Sutra प.3.2.145: प्रे लपसृद्रुमथवदवसः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — pre lapasfdrumaTavadavasaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.145"
SUTRA_TEXT = "प्रे लपसृद्रुमथवदवसः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — pre lapasfdrumaTavadavasaH"


class Sutra32145:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

