# Sutra प.7.2.23: घुषिरविशब्दने
# (Taddhita (secondary derivations)) — GuziraviSabdane

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.23"
SUTRA_TEXT = "घुषिरविशब्दने"
SUTRA_DESC = "(Taddhita (secondary derivations)) — GuziraviSabdane"


class Sutra7223:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.23: अग्निः'),
		('रामः', '', 'प.7.2.23: रामः'),
		('सीता', '', 'प.7.2.23: सीता'),
	]

