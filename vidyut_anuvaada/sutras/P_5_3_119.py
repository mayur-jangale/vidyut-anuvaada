# Sutra प.5.3.119: ञ्यादयस्तद्राजाः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — YyAdayastadrAjAH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.119"
SUTRA_TEXT = "ञ्यादयस्तद्राजाः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — YyAdayastadrAjAH"


class Sutra53119:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.119: अग्निः'),
		('रामः', '', 'प.5.3.119: रामः'),
		('सीता', '', 'प.5.3.119: सीता'),
	]

