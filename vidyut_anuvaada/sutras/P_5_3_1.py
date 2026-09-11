# Sutra प.5.3.1: प्राग्दिशो विभक्तिः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — prAgdiSo viBaktiH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.1"
SUTRA_TEXT = "प्राग्दिशो विभक्तिः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — prAgdiSo viBaktiH"


class Sutra531:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.1: अग्निः'),
		('रामः', '', 'प.5.3.1: रामः'),
		('सीता', '', 'प.5.3.1: सीता'),
	]

