# Sutra प.1.1.52: अलोऽन्त्यस्य
# (Samjna (technical definitions)) — alo'ntyasya

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.52"
SUTRA_TEXT = "अलोऽन्त्यस्य"
SUTRA_DESC = "(Samjna (technical definitions)) — alo'ntyasya"


class Sutra1152:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_52
		return apply_1_1_52(word, pos)

	EXAMPLES = [
		('अल', '', "प.1.1.52:alo'ntyasya;input=अल"),
		('अग्नि', '', "प.1.1.52:alo'ntyasya;input=अग्नि"),
	]

