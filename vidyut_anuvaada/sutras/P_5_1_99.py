# Sutra प.5.1.99: सम्पादिनि
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — sampAdini

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.99"
SUTRA_TEXT = "सम्पादिनि"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — sampAdini"


class Sutra5199:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.99: अग्निः'),
		('रामः', '', 'प.5.1.99: रामः'),
		('सीता', '', 'प.5.1.99: सीता'),
	]

