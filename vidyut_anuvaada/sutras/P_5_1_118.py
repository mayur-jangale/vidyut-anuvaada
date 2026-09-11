# Sutra प.5.1.118: उपसर्गाच्छन्दसि धात्वर्थे
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — upasargAcCandasi DAtvarTe

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.118"
SUTRA_TEXT = "उपसर्गाच्छन्दसि धात्वर्थे"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — upasargAcCandasi DAtvarTe"


class Sutra51118:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.118: अग्निः'),
		('रामः', '', 'प.5.1.118: रामः'),
		('सीता', '', 'प.5.1.118: सीता'),
	]

