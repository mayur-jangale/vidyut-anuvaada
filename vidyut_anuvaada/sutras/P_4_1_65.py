# Sutra प.4.1.65: इतो मनुष्यजातेः
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.65"
SUTRA_TEXT = "इतो मनुष्यजातेः"
SUTRA_DESC = "supaḥ — continued"


class Sutra4165:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

