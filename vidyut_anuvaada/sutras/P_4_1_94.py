# Sutra प.4.1.94: गोत्राद्यून्यस्त्रियाम्
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.94"
SUTRA_TEXT = "गोत्राद्यून्यस्त्रियाम्"
SUTRA_DESC = "supaḥ — continued"


class Sutra4194:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

