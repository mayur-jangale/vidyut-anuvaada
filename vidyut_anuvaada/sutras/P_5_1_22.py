# Sutra प.5.1.22: संख्याया अतिशदन्तायाः कन्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — saMKyAyA atiSadantAyAH kan

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.22"
SUTRA_TEXT = "संख्याया अतिशदन्तायाः कन्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — saMKyAyA atiSadantAyAH kan"


class Sutra5122:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.22: अग्निः'),
		('रामः', '', 'प.5.1.22: रामः'),
		('सीता', '', 'प.5.1.22: सीता'),
	]

