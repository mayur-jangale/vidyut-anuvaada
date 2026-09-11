# Sutra प.5.3.76: अनुकम्पायाम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — anukampAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.76"
SUTRA_TEXT = "अनुकम्पायाम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — anukampAyAm"


class Sutra5376:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.76: अग्निः'),
		('रामः', '', 'प.5.3.76: रामः'),
		('सीता', '', 'प.5.3.76: सीता'),
	]

