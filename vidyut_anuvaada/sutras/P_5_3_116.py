# Sutra प.5.3.116: दामन्यादित्रिगर्तषष्ठाच्छः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — dAmanyAditrigartazazWAcCaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.116"
SUTRA_TEXT = "दामन्यादित्रिगर्तषष्ठाच्छः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — dAmanyAditrigartazazWAcCaH"


class Sutra53116:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.116: अग्निः'),
		('रामः', '', 'प.5.3.116: रामः'),
		('सीता', '', 'प.5.3.116: सीता'),
	]

