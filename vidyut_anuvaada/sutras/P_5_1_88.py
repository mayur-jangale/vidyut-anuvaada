# Sutra प.5.1.88: वर्षाल्लुक् च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — varzAlluk ca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.88"
SUTRA_TEXT = "वर्षाल्लुक् च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — varzAlluk ca"


class Sutra5188:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.88: अग्निः'),
		('रामः', '', 'प.5.1.88: रामः'),
		('सीता', '', 'प.5.1.88: सीता'),
	]

