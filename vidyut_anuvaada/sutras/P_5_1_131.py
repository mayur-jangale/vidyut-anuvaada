# Sutra प.5.1.131: इगन्ताच्च लघुपूर्वात्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — igantAcca laGupUrvAt

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.131"
SUTRA_TEXT = "इगन्ताच्च लघुपूर्वात्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — igantAcca laGupUrvAt"


class Sutra51131:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.131: अग्निः'),
		('रामः', '', 'प.5.1.131: रामः'),
		('सीता', '', 'प.5.1.131: सीता'),
	]

