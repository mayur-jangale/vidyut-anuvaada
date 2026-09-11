# Sutra प.5.4.143: स्त्रियां संज्ञायाम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — striyAM saMjYAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.143"
SUTRA_TEXT = "स्त्रियां संज्ञायाम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — striyAM saMjYAyAm"


class Sutra54143:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.143: अग्निः'),
		('रामः', '', 'प.5.4.143: रामः'),
		('सीता', '', 'प.5.4.143: सीता'),
	]

