# Sutra प.5.1.12: तदर्थं विकृतेः प्रकृतौ
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — tadarTaM vikfteH prakftO

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.12"
SUTRA_TEXT = "तदर्थं विकृतेः प्रकृतौ"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — tadarTaM vikfteH prakftO"


class Sutra5112:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.12: अग्निः'),
		('रामः', '', 'प.5.1.12: रामः'),
		('सीता', '', 'प.5.1.12: सीता'),
	]

