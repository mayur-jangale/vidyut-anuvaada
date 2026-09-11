# Sutra प.5.4.133: वा संज्ञायाम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — vA saMjYAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.133"
SUTRA_TEXT = "वा संज्ञायाम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — vA saMjYAyAm"


class Sutra54133:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.133: अग्निः'),
		('रामः', '', 'प.5.4.133: रामः'),
		('सीता', '', 'प.5.4.133: सीता'),
	]

