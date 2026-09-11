# Sutra प.5.3.63: अन्तिकबाढयोर्नेदसाधौ
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — antikabAQayornedasADO

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.63"
SUTRA_TEXT = "अन्तिकबाढयोर्नेदसाधौ"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — antikabAQayornedasADO"


class Sutra5363:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.63: अग्निः'),
		('रामः', '', 'प.5.3.63: रामः'),
		('सीता', '', 'प.5.3.63: सीता'),
	]

