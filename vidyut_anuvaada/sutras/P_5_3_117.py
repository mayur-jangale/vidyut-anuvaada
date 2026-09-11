# Sutra प.5.3.117: पर्श्वादियौधेयादिभ्यामणञौ
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — parSvAdiyODeyAdiByAmaRaYO

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.117"
SUTRA_TEXT = "पर्श्वादियौधेयादिभ्यामणञौ"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — parSvAdiyODeyAdiByAmaRaYO"


class Sutra53117:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.117: अग्निः'),
		('रामः', '', 'प.5.3.117: रामः'),
		('सीता', '', 'प.5.3.117: सीता'),
	]

