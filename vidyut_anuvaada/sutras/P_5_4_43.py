# Sutra प.5.4.43: संख्यैकवचनाच्च वीप्सायाम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — saMKyEkavacanAcca vIpsAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.43"
SUTRA_TEXT = "संख्यैकवचनाच्च वीप्सायाम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — saMKyEkavacanAcca vIpsAyAm"


class Sutra5443:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.43: अग्निः'),
		('रामः', '', 'प.5.4.43: रामः'),
		('सीता', '', 'प.5.4.43: सीता'),
	]

