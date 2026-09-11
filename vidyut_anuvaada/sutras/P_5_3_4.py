# Sutra प.5.3.4: एतेतौ रथोः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — etetO raToH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.4"
SUTRA_TEXT = "एतेतौ रथोः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — etetO raToH"


class Sutra534:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.4: अग्निः'),
		('रामः', '', 'प.5.3.4: रामः'),
		('सीता', '', 'प.5.3.4: सीता'),
	]

