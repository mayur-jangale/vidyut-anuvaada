# Sutra प.5.2.53: वतोरिथुक्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — vatoriTuk

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.53"
SUTRA_TEXT = "वतोरिथुक्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — vatoriTuk"


class Sutra5253:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.53: अग्निः'),
		('रामः', '', 'प.5.2.53: रामः'),
		('सीता', '', 'प.5.2.53: सीता'),
	]

