# Sutra प.5.4.136: अल्पाख्यायाम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — alpAKyAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.136"
SUTRA_TEXT = "अल्पाख्यायाम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — alpAKyAyAm"


class Sutra54136:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.136: अग्निः'),
		('रामः', '', 'प.5.4.136: रामः'),
		('सीता', '', 'प.5.4.136: सीता'),
	]

