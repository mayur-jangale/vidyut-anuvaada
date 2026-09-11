# Sutra प.5.2.22: साप्तपदीनं सख्यम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — sAptapadInaM saKyam

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.22"
SUTRA_TEXT = "साप्तपदीनं सख्यम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — sAptapadInaM saKyam"


class Sutra5222:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.22: अग्निः'),
		('रामः', '', 'प.5.2.22: रामः'),
		('सीता', '', 'प.5.2.22: सीता'),
	]

