# Sutra प.1.1.63: न लुमताङ्गस्य
# (Samjna (technical definitions)) — na lumatANgasya

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.63"
SUTRA_TEXT = "न लुमताङ्गस्य"
SUTRA_DESC = "(Samjna (technical definitions)) — na lumatANgasya"


class Sutra1163:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_63
		return apply_1_1_63(word, pos)

	EXAMPLES = [
		('लुमत्', '', 'प.1.1.63:na-lumatāṅgasya;input=लुमत्'),
		('अग्नि', '', 'प.1.1.63:na-lumatāṅgasya;input=अग्नि'),
	]

