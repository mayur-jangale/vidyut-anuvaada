# Sutra प.5.3.105: कुशाग्राच्छः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — kuSAgrAcCaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.105"
SUTRA_TEXT = "कुशाग्राच्छः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — kuSAgrAcCaH"


class Sutra53105:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.105: अग्निः'),
		('रामः', '', 'प.5.3.105: रामः'),
		('सीता', '', 'प.5.3.105: सीता'),
	]

