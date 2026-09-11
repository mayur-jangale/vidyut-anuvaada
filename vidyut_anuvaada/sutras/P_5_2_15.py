# Sutra प.5.2.15: अनुग्वलंगामी
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — anugvalaMgAmI

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.15"
SUTRA_TEXT = "अनुग्वलंगामी"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — anugvalaMgAmI"


class Sutra5215:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.15: अग्निः'),
		('रामः', '', 'प.5.2.15: रामः'),
		('सीता', '', 'प.5.2.15: सीता'),
	]

