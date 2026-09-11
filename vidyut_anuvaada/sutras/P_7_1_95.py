# Sutra प.7.1.95: तृज्वत् क्रोष्टुः
# (Taddhita (secondary derivations)) — tfjvat krozwuH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.95"
SUTRA_TEXT = "तृज्वत् क्रोष्टुः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — tfjvat krozwuH"


class Sutra7195:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.95: अग्निः'),
		('रामः', '', 'प.7.1.95: रामः'),
		('सीता', '', 'प.7.1.95: सीता'),
	]

