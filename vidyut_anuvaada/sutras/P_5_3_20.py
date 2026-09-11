# Sutra प.5.3.20: तयोर्दार्हिलौ च च्छन्दसि
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — tayordArhilO ca cCandasi

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.20"
SUTRA_TEXT = "तयोर्दार्हिलौ च च्छन्दसि"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — tayordArhilO ca cCandasi"


class Sutra5320:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.20: अग्निः'),
		('रामः', '', 'प.5.3.20: रामः'),
		('सीता', '', 'प.5.3.20: सीता'),
	]

