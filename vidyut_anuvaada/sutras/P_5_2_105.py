# Sutra प.5.2.105: देशे लुबिलचौ च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — deSe lubilacO ca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.105"
SUTRA_TEXT = "देशे लुबिलचौ च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — deSe lubilacO ca"


class Sutra52105:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.105: अग्निः'),
		('रामः', '', 'प.5.2.105: रामः'),
		('सीता', '', 'प.5.2.105: सीता'),
	]

