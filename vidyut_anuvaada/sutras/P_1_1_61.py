# Sutra प.1.1.61: प्रत्ययस्य लुक्श्लुलुपः
# (Samjna (technical definitions)) — pratyayasya lukSlulupaH

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.61"
SUTRA_TEXT = "प्रत्ययस्य लुक्श्लुलुपः"
SUTRA_DESC = "(Samjna (technical definitions)) — pratyayasya lukSlulupaH"


class Sutra1161:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_61
		return apply_1_1_61(word, pos)

	EXAMPLES = [
		('अग्नि', 'luk', 'pratyaya-lopa:LUK:अग्नि'),
		('देव', 'ślu', 'pratyaya-lopa:ŚLU:देव'),
		('वाक्', '', 'no-lopa:वाक्'),
	]

