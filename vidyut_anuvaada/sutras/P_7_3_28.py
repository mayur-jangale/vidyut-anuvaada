# Sutra प.7.3.28: प्रवाहणस्य ढे
# (Taddhita (secondary derivations)) — pravAhaRasya Qe

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.28"
SUTRA_TEXT = "प्रवाहणस्य ढे"
SUTRA_DESC = "(Taddhita (secondary derivations)) — pravAhaRasya Qe"


class Sutra7328:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.28: अग्निः'),
		('रामः', '', 'प.7.3.28: रामः'),
		('सीता', '', 'प.7.3.28: सीता'),
	]

