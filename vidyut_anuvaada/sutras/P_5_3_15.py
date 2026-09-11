# Sutra प.5.3.15: सर्वैकान्यकिंयत्तदः काले दा
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — sarvEkAnyakiMyattadaH kAle dA

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.15"
SUTRA_TEXT = "सर्वैकान्यकिंयत्तदः काले दा"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — sarvEkAnyakiMyattadaH kAle dA"


class Sutra5315:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.15: अग्निः'),
		('रामः', '', 'प.5.3.15: रामः'),
		('सीता', '', 'प.5.3.15: सीता'),
	]

