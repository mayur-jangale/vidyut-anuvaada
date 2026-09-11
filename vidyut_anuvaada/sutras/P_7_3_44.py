# Sutra प.7.3.44: प्रत्ययस्थात् कात् पूर्वस्यात इदाप्यसुपः
# (Taddhita (secondary derivations)) — pratyayasTAt kAt pUrvasyAta idApyasupaH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.44"
SUTRA_TEXT = "प्रत्ययस्थात् कात् पूर्वस्यात इदाप्यसुपः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — pratyayasTAt kAt pUrvasyAta idApyasupaH"


class Sutra7344:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.44: अग्निः'),
		('रामः', '', 'प.7.3.44: रामः'),
		('सीता', '', 'प.7.3.44: सीता'),
	]

