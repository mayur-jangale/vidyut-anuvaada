# Sutra प.3.3.4: यावत्पुरानिपातयोर्लट्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — yAvatpurAnipAtayorlaw

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.4"
SUTRA_TEXT = "यावत्पुरानिपातयोर्लट्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — yAvatpurAnipAtayorlaw"


class Sutra334:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

