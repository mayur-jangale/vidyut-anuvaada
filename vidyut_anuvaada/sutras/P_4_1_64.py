# Sutra प.4.1.64: पाककर्णपर्णपुष्पफलमूलवालोत्तरपदाच्च
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.64"
SUTRA_TEXT = "पाककर्णपर्णपुष्पफलमूलवालोत्तरपदाच्च"
SUTRA_DESC = "supaḥ — continued"


class Sutra4164:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

