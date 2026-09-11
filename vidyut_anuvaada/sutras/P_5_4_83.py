# Sutra प.5.4.83: अनुगवमायामे
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — anugavamAyAme

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.83"
SUTRA_TEXT = "अनुगवमायामे"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — anugavamAyAme"


class Sutra5483:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.83: अग्निः'),
		('रामः', '', 'प.5.4.83: रामः'),
		('सीता', '', 'प.5.4.83: सीता'),
	]

