# Sutra प.5.4.29: यावादिभ्यः कन्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — yAvAdiByaH kan

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.29"
SUTRA_TEXT = "यावादिभ्यः कन्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — yAvAdiByaH kan"


class Sutra5429:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.29: अग्निः'),
		('रामः', '', 'प.5.4.29: रामः'),
		('सीता', '', 'प.5.4.29: सीता'),
	]

