# Sutra प.5.4.93: अग्राख्यायामुरसः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — agrAKyAyAmurasaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.93"
SUTRA_TEXT = "अग्राख्यायामुरसः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — agrAKyAyAmurasaH"


class Sutra5493:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.93: अग्निः'),
		('रामः', '', 'प.5.4.93: रामः'),
		('सीता', '', 'प.5.4.93: सीता'),
	]

