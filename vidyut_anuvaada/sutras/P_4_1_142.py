# Sutra प.4.1.142: दुष्कुलाड्ढक्
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.142"
SUTRA_TEXT = "दुष्कुलाड्ढक्"
SUTRA_DESC = "supaḥ — continued"


class Sutra41142:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

