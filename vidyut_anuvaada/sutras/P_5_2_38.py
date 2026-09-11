# Sutra प.5.2.38: पुरुषहस्तिभ्यामण् च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — puruzahastiByAmaR ca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.38"
SUTRA_TEXT = "पुरुषहस्तिभ्यामण् च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — puruzahastiByAmaR ca"


class Sutra5238:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.38: अग्निः'),
		('रामः', '', 'प.5.2.38: रामः'),
		('सीता', '', 'प.5.2.38: सीता'),
	]

