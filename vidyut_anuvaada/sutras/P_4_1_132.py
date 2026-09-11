# Sutra प.4.1.132: पितृष्वसुश्छण्
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.132"
SUTRA_TEXT = "पितृष्वसुश्छण्"
SUTRA_DESC = "supaḥ — continued"


class Sutra41132:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

