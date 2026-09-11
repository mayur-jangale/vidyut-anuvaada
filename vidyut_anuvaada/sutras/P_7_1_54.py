# Sutra प.7.1.54: ह्रस्वनद्यापो नुट्
# (Taddhita (secondary derivations)) — hrasvanadyApo nuw

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.54"
SUTRA_TEXT = "ह्रस्वनद्यापो नुट्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — hrasvanadyApo nuw"


class Sutra7154:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.54: अग्निः'),
		('रामः', '', 'प.7.1.54: रामः'),
		('सीता', '', 'प.7.1.54: सीता'),
	]

