# Sutra प.4.1.86: उत्सादिभ्योऽञ्
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.86"
SUTRA_TEXT = "उत्सादिभ्योऽञ्"
SUTRA_DESC = "supaḥ — continued"


class Sutra4186:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

