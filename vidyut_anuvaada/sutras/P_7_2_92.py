# Sutra प.7.2.92: युवावौ द्विवचने
# (Taddhita (secondary derivations)) — yuvAvO dvivacane

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.92"
SUTRA_TEXT = "युवावौ द्विवचने"
SUTRA_DESC = "(Taddhita (secondary derivations)) — yuvAvO dvivacane"


class Sutra7292:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.92: अग्निः'),
		('रामः', '', 'प.7.2.92: रामः'),
		('सीता', '', 'प.7.2.92: सीता'),
	]

