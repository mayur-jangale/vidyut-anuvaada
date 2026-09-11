# Sutra प.4.1.67: बाह्वन्तात् संज्ञायाम्
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.67"
SUTRA_TEXT = "बाह्वन्तात् संज्ञायाम्"
SUTRA_DESC = "supaḥ — continued"


class Sutra4167:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

