# Sutra प.3.2.171: आदृगमहनजनः किकिनौ लिट् च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — AdfgamahanajanaH kikinO liw ca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.171"
SUTRA_TEXT = "आदृगमहनजनः किकिनौ लिट् च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — AdfgamahanajanaH kikinO liw ca"


class Sutra32171:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

