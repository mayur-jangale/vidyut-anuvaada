# Sutra प.5.4.92: गोरतद्धितलुकि
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — goratadDitaluki

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.92"
SUTRA_TEXT = "गोरतद्धितलुकि"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — goratadDitaluki"


class Sutra5492:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.92: अग्निः'),
		('रामः', '', 'प.5.4.92: रामः'),
		('सीता', '', 'प.5.4.92: सीता'),
	]

