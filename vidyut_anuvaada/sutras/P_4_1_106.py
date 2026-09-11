# Sutra प.4.1.106: मधुबभ्र्वोर्ब्राह्मणकौशिकयोः
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.106"
SUTRA_TEXT = "मधुबभ्र्वोर्ब्राह्मणकौशिकयोः"
SUTRA_DESC = "supaḥ — continued"


class Sutra41106:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

