# Sutra प.5.4.36: तद्युक्तात् कर्मणोऽण्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — tadyuktAt karmaRo'R

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.36"
SUTRA_TEXT = "तद्युक्तात् कर्मणोऽण्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — tadyuktAt karmaRo'R"


class Sutra5436:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.36: अग्निः'),
		('रामः', '', 'प.5.4.36: रामः'),
		('सीता', '', 'प.5.4.36: सीता'),
	]

