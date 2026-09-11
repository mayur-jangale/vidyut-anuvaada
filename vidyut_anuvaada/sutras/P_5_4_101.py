# Sutra प.5.4.101: खार्याः प्राचाम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — KAryAH prAcAm

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.101"
SUTRA_TEXT = "खार्याः प्राचाम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — KAryAH prAcAm"


class Sutra54101:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.101: अग्निः'),
		('रामः', '', 'प.5.4.101: रामः'),
		('सीता', '', 'प.5.4.101: सीता'),
	]

