# Sutra प.4.1.102: शरद्वच्छुनकदर्भाद्भृगुवत्साग्रायणेषु
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.102"
SUTRA_TEXT = "शरद्वच्छुनकदर्भाद्भृगुवत्साग्रायणेषु"
SUTRA_DESC = "supaḥ — continued"


class Sutra41102:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

