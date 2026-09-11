# Sutra प.7.3.71: ओतः श्यनि
# (Taddhita (secondary derivations)) — otaH Syani

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.71"
SUTRA_TEXT = "ओतः श्यनि"
SUTRA_DESC = "(Taddhita (secondary derivations)) — otaH Syani"


class Sutra7371:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.71: अग्निः'),
		('रामः', '', 'प.7.3.71: रामः'),
		('सीता', '', 'प.7.3.71: सीता'),
	]

