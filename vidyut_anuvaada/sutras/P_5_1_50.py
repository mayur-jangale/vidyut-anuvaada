# Sutra प.5.1.50: तद्धरति वहत्यावहति भाराद्वंशादिभ्यः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — tadDarati vahatyAvahati BArAdvaMSAdiByaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.50"
SUTRA_TEXT = "तद्धरति वहत्यावहति भाराद्वंशादिभ्यः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — tadDarati vahatyAvahati BArAdvaMSAdiByaH"


class Sutra5150:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.50: अग्निः'),
		('रामः', '', 'प.5.1.50: रामः'),
		('सीता', '', 'प.5.1.50: सीता'),
	]

