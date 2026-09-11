# Sutra प.1.1.66: तस्मिन्निति निर्दिष्टे पूर्वस्य
# (Samjna (technical definitions)) — tasminniti nirdizwe pUrvasya

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.66"
SUTRA_TEXT = "तस्मिन्निति निर्दिष्टे पूर्वस्य"
SUTRA_DESC = "(Samjna (technical definitions)) — tasminniti nirdizwe pUrvasya"


class Sutra1166:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_66
		return apply_1_1_66(word, pos)

	EXAMPLES = [
		('अग्निः', '', 'previous-element-applied:अग्निः'),
	]

