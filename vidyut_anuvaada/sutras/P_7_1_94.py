# Sutra प.7.1.94: ऋदुशनस्पुरुदंसोऽनेहसां च
# (Taddhita (secondary derivations)) — fduSanaspurudaMso'nehasAM ca

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.94"
SUTRA_TEXT = "ऋदुशनस्पुरुदंसोऽनेहसां च"
SUTRA_DESC = "(Taddhita (secondary derivations)) — fduSanaspurudaMso'nehasAM ca"


class Sutra7194:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.94: अग्निः'),
		('रामः', '', 'प.7.1.94: रामः'),
		('सीता', '', 'प.7.1.94: सीता'),
	]

