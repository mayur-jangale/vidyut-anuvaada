# Sutra प.4.1.12: अनो बहुव्रीहेः
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.12"
SUTRA_TEXT = "अनो बहुव्रीहेः"
SUTRA_DESC = "supaḥ — continued"


class Sutra4112:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

