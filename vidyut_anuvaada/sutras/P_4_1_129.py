# Sutra प.4.1.129: गोधाया ढ्रक्
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.129"
SUTRA_TEXT = "गोधाया ढ्रक्"
SUTRA_DESC = "supaḥ — continued"


class Sutra41129:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

