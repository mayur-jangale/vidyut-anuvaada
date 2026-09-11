# Sutra प.5.2.23: हैयंगवीनं संज्ञायाम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — hEyaMgavInaM saMjYAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.23"
SUTRA_TEXT = "हैयंगवीनं संज्ञायाम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — hEyaMgavInaM saMjYAyAm"


class Sutra5223:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.23: अग्निः'),
		('रामः', '', 'प.5.2.23: रामः'),
		('सीता', '', 'प.5.2.23: सीता'),
	]

