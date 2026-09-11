# Sutra प.1.1.8: मुखनासिकावचनोऽनुनासिकः
# A nasal articulated through both nose and mouth is called anunāsika

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.8"
SUTRA_TEXT = "मुखनासिकावचनोऽनुनासिकः"
SUTRA_DESC = "A nasal articulated through both nose and mouth is called anunāsika"


class Sutra118:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_8
		return apply_1_1_8(word, pos)

	EXAMPLES = [
		('अनुस्वार', '', 'anunāsika=न'),
		('मध्ये', '', 'anunāsika=म'),
		('वाक्', '', 'anunāsika=none'),
	]

