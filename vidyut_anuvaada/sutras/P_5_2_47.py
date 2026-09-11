# Sutra प.5.2.47: संख्याया गुणस्य निमाने मयट्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — saMKyAyA guRasya nimAne mayaw

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.47"
SUTRA_TEXT = "संख्याया गुणस्य निमाने मयट्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — saMKyAyA guRasya nimAne mayaw"


class Sutra5247:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.47: अग्निः'),
		('रामः', '', 'प.5.2.47: रामः'),
		('सीता', '', 'प.5.2.47: सीता'),
	]

