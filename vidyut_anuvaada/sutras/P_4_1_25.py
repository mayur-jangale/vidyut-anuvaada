# Sutra प.4.1.25: बहुव्रीहेरूधसो ङीष्
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.25"
SUTRA_TEXT = "बहुव्रीहेरूधसो ङीष्"
SUTRA_DESC = "supaḥ — continued"


class Sutra4125:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

