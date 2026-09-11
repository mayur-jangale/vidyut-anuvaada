# Sutra प.5.4.96: अतेः शुनः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — ateH SunaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.96"
SUTRA_TEXT = "अतेः शुनः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — ateH SunaH"


class Sutra5496:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.96: अग्निः'),
		('रामः', '', 'प.5.4.96: रामः'),
		('सीता', '', 'प.5.4.96: सीता'),
	]

