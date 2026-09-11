# Sutra प.7.3.74: शमामष्टानां दीर्घः श्यनि
# (Taddhita (secondary derivations)) — SamAmazwAnAM dIrGaH Syani

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.74"
SUTRA_TEXT = "शमामष्टानां दीर्घः श्यनि"
SUTRA_DESC = "(Taddhita (secondary derivations)) — SamAmazwAnAM dIrGaH Syani"


class Sutra7374:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.74: अग्निः'),
		('रामः', '', 'प.7.3.74: रामः'),
		('सीता', '', 'प.7.3.74: सीता'),
	]

