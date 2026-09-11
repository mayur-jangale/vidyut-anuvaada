# Sutra प.3.4.28: यथातथयोरसूयाप्रतिवचने
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — yaTAtaTayorasUyAprativacane

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.28"
SUTRA_TEXT = "यथातथयोरसूयाप्रतिवचने"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — yaTAtaTayorasUyAprativacane"


class Sutra3428:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

