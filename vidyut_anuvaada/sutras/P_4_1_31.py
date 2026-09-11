# Sutra प.4.1.31: रात्रेश्चाजसौ
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.31"
SUTRA_TEXT = "रात्रेश्चाजसौ"
SUTRA_DESC = "supaḥ — continued"


class Sutra4131:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

