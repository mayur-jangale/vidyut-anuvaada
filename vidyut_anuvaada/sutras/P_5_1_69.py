# Sutra प.5.1.69: कडङ्करदक्षिणाच्छ च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — kaqaNkaradakziRAcCa ca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.69"
SUTRA_TEXT = "कडङ्करदक्षिणाच्छ च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — kaqaNkaradakziRAcCa ca"


class Sutra5169:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.69: अग्निः'),
		('रामः', '', 'प.5.1.69: रामः'),
		('सीता', '', 'प.5.1.69: सीता'),
	]

