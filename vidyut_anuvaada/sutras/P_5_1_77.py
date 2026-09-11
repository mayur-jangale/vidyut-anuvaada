# Sutra प.5.1.77: उत्तरपथेनाहृतं च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — uttarapaTenAhftaM ca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.77"
SUTRA_TEXT = "उत्तरपथेनाहृतं च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — uttarapaTenAhftaM ca"


class Sutra5177:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.77: अग्निः'),
		('रामः', '', 'प.5.1.77: रामः'),
		('सीता', '', 'प.5.1.77: सीता'),
	]

