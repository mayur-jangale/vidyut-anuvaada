# Sutra प.1.2.8: रुदविदमुषग्रहिस्वपिप्रच्छः सँश्च
# (Samjna (technical definitions)) — rudavidamuzagrahisvapipracCaH sa~Sca

from P_1_2 import apply_1_2_8

SUTRA_CODE = "प.1.2.8"
SUTRA_TEXT = "रुदविदमुषग्रहिस्वपिप्रच्छः सँश्च"
SUTRA_DESC = "(Samjna (technical definitions)) — rudavidamuzagrahisvapipracCaH sa~Sca"


class Sutra128:
	def apply(self, word, pos):
		return apply_1_2_8(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-rudādi:अग्निः'),
		('रामः', '', 'non-rudādi:रामः'),
		('सीता', '', 'non-rudādi:सीता'),
	]

