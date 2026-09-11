# Sutra प.7.3.34: नोदात्तोपदेशस्य मान्तस्यानाचमेः
# (Taddhita (secondary derivations)) — nodAttopadeSasya mAntasyAnAcameH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.34"
SUTRA_TEXT = "नोदात्तोपदेशस्य मान्तस्यानाचमेः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — nodAttopadeSasya mAntasyAnAcameH"


class Sutra7334:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.34: अग्निः'),
		('रामः', '', 'प.7.3.34: रामः'),
		('सीता', '', 'प.7.3.34: सीता'),
	]

