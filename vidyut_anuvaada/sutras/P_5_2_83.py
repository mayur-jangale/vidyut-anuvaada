# Sutra प.5.2.83: कुल्माषादञ्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — kulmAzAdaY

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.83"
SUTRA_TEXT = "कुल्माषादञ्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — kulmAzAdaY"


class Sutra5283:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.83: अग्निः'),
		('रामः', '', 'प.5.2.83: रामः'),
		('सीता', '', 'प.5.2.83: सीता'),
	]

