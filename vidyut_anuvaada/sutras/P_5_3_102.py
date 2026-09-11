# Sutra प.5.3.102: शिलाया ढः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — SilAyA QaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.102"
SUTRA_TEXT = "शिलाया ढः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — SilAyA QaH"


class Sutra53102:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.102: अग्निः'),
		('रामः', '', 'प.5.3.102: रामः'),
		('सीता', '', 'प.5.3.102: सीता'),
	]

