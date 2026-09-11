# Sutra प.5.4.37: ओषधेरजातौ
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — ozaDerajAtO

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.37"
SUTRA_TEXT = "ओषधेरजातौ"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — ozaDerajAtO"


class Sutra5437:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.37: अग्निः'),
		('रामः', '', 'प.5.4.37: रामः'),
		('सीता', '', 'प.5.4.37: सीता'),
	]

