# Sutra प.5.2.46: शदन्तविंशतेश्च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — SadantaviMSateSca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.46"
SUTRA_TEXT = "शदन्तविंशतेश्च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — SadantaviMSateSca"


class Sutra5246:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.46: अग्निः'),
		('रामः', '', 'प.5.2.46: रामः'),
		('सीता', '', 'प.5.2.46: सीता'),
	]

