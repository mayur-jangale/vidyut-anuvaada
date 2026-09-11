# Sutra प.1.1.38: तद्धितश्चासर्वविभक्तिः
# sup — the 21 nominal case endings (सु, औ, जस्, etc.)

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.38"
SUTRA_TEXT = "तद्धितश्चासर्वविभक्तिः"
SUTRA_DESC = "sup — the 21 nominal case endings (सु, औ, जस्, etc.)"


class Sutra1138:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_38
		return apply_1_1_38(word, pos)

	EXAMPLES = [
		('सु', '', 'sup:सु;sup-pratyaya'),
		('जस्', '', 'sup:जस्;sup-pratyaya'),
		('औ', '', 'sup:औ;sup-pratyaya'),
		('तिप्', '', 'non-sup:तिप्'),
	]

