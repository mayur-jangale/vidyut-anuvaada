# Sutra प.5.2.92: क्षेत्रियच् परक्षेत्रे चिकित्स्यः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — kzetriyac parakzetre cikitsyaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.92"
SUTRA_TEXT = "क्षेत्रियच् परक्षेत्रे चिकित्स्यः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — kzetriyac parakzetre cikitsyaH"


class Sutra5292:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.92: अग्निः'),
		('रामः', '', 'प.5.2.92: रामः'),
		('सीता', '', 'प.5.2.92: सीता'),
	]

