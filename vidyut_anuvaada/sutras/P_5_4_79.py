# Sutra प.5.4.79: अवसमन्धेभ्यस्तमसः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — avasamanDeByastamasaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.79"
SUTRA_TEXT = "अवसमन्धेभ्यस्तमसः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — avasamanDeByastamasaH"


class Sutra5479:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.79: अग्निः'),
		('रामः', '', 'प.5.4.79: रामः'),
		('सीता', '', 'प.5.4.79: सीता'),
	]

