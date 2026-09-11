# Sutra प.4.1.49: इन्द्रवरुणभवशर्वरुद्रमृडहिमारण्ययवयवनमातुलाचार्याणामानुक्
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.49"
SUTRA_TEXT = "इन्द्रवरुणभवशर्वरुद्रमृडहिमारण्ययवयवनमातुलाचार्याणामानुक्"
SUTRA_DESC = "supaḥ — continued"


class Sutra4149:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

