# Sutra प.5.2.80: उत्क उन्मनाः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — utka unmanAH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.80"
SUTRA_TEXT = "उत्क उन्मनाः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — utka unmanAH"


class Sutra5280:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.80: अग्निः'),
		('रामः', '', 'प.5.2.80: रामः'),
		('सीता', '', 'प.5.2.80: सीता'),
	]

