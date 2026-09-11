# Sutra प.5.4.22: समूहवच्च बहुषु
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — samUhavacca bahuzu

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.22"
SUTRA_TEXT = "समूहवच्च बहुषु"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — samUhavacca bahuzu"


class Sutra5422:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.22: अग्निः'),
		('रामः', '', 'प.5.4.22: रामः'),
		('सीता', '', 'प.5.4.22: सीता'),
	]

