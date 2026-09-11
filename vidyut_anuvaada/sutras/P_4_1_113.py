# Sutra प.4.1.113: अवृद्धाभ्यो नदीमानुषीभ्यस्तन्नामिकाभ्यः
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.113"
SUTRA_TEXT = "अवृद्धाभ्यो नदीमानुषीभ्यस्तन्नामिकाभ्यः"
SUTRA_DESC = "supaḥ — continued"


class Sutra41113:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

