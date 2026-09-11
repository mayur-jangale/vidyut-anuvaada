# Sutra प.7.2.94: त्वाहौ सौ
# (Taddhita (secondary derivations)) — tvAhO sO

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.94"
SUTRA_TEXT = "त्वाहौ सौ"
SUTRA_DESC = "(Taddhita (secondary derivations)) — tvAhO sO"


class Sutra7294:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.94: अग्निः'),
		('रामः', '', 'प.7.2.94: रामः'),
		('सीता', '', 'प.7.2.94: सीता'),
	]

