# Sutra प.5.4.155: न संज्ञायाम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — na saMjYAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.155"
SUTRA_TEXT = "न संज्ञायाम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — na saMjYAyAm"


class Sutra54155:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.155: अग्निः'),
		('रामः', '', 'प.5.4.155: रामः'),
		('सीता', '', 'प.5.4.155: सीता'),
	]

