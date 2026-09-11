# Sutra प.5.2.12: समांसमां विजायते
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — samAMsamAM vijAyate

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.12"
SUTRA_TEXT = "समांसमां विजायते"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — samAMsamAM vijAyate"


class Sutra5212:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.12: अग्निः'),
		('रामः', '', 'प.5.2.12: रामः'),
		('सीता', '', 'प.5.2.12: सीता'),
	]

