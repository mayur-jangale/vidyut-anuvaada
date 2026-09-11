# Sutra प.4.1.59: दीर्घजिह्वी च च्छन्दसि
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.59"
SUTRA_TEXT = "दीर्घजिह्वी च च्छन्दसि"
SUTRA_DESC = "supaḥ — continued"


class Sutra4159:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

