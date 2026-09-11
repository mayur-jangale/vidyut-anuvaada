# Sutra प.5.1.124: गुणवचनब्राह्मणादिभ्यः कर्मणि च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — guRavacanabrAhmaRAdiByaH karmaRi ca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.124"
SUTRA_TEXT = "गुणवचनब्राह्मणादिभ्यः कर्मणि च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — guRavacanabrAhmaRAdiByaH karmaRi ca"


class Sutra51124:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.124: अग्निः'),
		('रामः', '', 'प.5.1.124: रामः'),
		('सीता', '', 'प.5.1.124: सीता'),
	]

