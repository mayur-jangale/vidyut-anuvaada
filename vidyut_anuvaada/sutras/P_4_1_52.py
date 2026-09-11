# Sutra प.4.1.52: बहुव्रीहेश्चान्तोदात्तात्
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.52"
SUTRA_TEXT = "बहुव्रीहेश्चान्तोदात्तात्"
SUTRA_DESC = "supaḥ — continued"


class Sutra4152:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

