# Sutra प.5.2.78: स एषां ग्रामणीः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — sa ezAM grAmaRIH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.78"
SUTRA_TEXT = "स एषां ग्रामणीः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — sa ezAM grAmaRIH"


class Sutra5278:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.78: अग्निः'),
		('रामः', '', 'प.5.2.78: रामः'),
		('सीता', '', 'प.5.2.78: सीता'),
	]

