# Sutra प.1.1.72: येन विधिस्तदन्तस्य
# (Samjna (technical definitions)) — yena viDistadantasya

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.72"
SUTRA_TEXT = "येन विधिस्तदन्तस्य"
SUTRA_DESC = "(Samjna (technical definitions)) — yena viDistadantasya"


class Sutra1172:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_72
		return apply_1_1_72(word, pos)

	EXAMPLES = [
		('येन', '', 'प.1.1.72:yena-vidhistadantasya;input=येन'),
		('अग्नि', '', 'प.1.1.72:yena-vidhistadantasya;input=अग्नि'),
	]

