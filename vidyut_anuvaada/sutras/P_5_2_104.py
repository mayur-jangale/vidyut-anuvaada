# Sutra प.5.2.104: सिकताशर्कराभ्यां च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — sikatASarkarAByAM ca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.104"
SUTRA_TEXT = "सिकताशर्कराभ्यां च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — sikatASarkarAByAM ca"


class Sutra52104:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.104: अग्निः'),
		('रामः', '', 'प.5.2.104: रामः'),
		('सीता', '', 'प.5.2.104: सीता'),
	]

