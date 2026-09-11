# Sutra प.1.1.70: तपरस्तत्कालस्य
# (Samjna (technical definitions)) — taparastatkAlasya

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.70"
SUTRA_TEXT = "तपरस्तत्कालस्य"
SUTRA_DESC = "(Samjna (technical definitions)) — taparastatkAlasya"


class Sutra1170:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_70
		return apply_1_1_70(word, pos)

	EXAMPLES = [
		('तपर', '', 'प.1.1.70:taparastatkālasya;input=तपर'),
		('अग्नि', '', 'प.1.1.70:taparastatkālasya;input=अग्नि'),
	]

