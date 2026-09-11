# Sutra प.5.2.49: नान्तादसंख्यादेर्मट्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — nAntAdasaMKyAdermaw

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.49"
SUTRA_TEXT = "नान्तादसंख्यादेर्मट्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — nAntAdasaMKyAdermaw"


class Sutra5249:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.49: अग्निः'),
		('रामः', '', 'प.5.2.49: रामः'),
		('सीता', '', 'प.5.2.49: सीता'),
	]

