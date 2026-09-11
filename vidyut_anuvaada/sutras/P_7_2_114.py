# Sutra प.7.2.114: मृजेर्वृद्धिः
# (Taddhita (secondary derivations)) — mfjervfdDiH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.114"
SUTRA_TEXT = "मृजेर्वृद्धिः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — mfjervfdDiH"


class Sutra72114:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.114: अग्निः'),
		('रामः', '', 'प.7.2.114: रामः'),
		('सीता', '', 'प.7.2.114: सीता'),
	]

