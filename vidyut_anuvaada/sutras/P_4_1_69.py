# Sutra प.4.1.69: ऊरूत्तरपदादौपम्ये
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.69"
SUTRA_TEXT = "ऊरूत्तरपदादौपम्ये"
SUTRA_DESC = "supaḥ — continued"


class Sutra4169:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

