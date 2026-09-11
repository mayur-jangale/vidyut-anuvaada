# Sutra प.4.1.124: विकर्णकुषीतकात् काश्यपे
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.124"
SUTRA_TEXT = "विकर्णकुषीतकात् काश्यपे"
SUTRA_DESC = "supaḥ — continued"


class Sutra41124:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

