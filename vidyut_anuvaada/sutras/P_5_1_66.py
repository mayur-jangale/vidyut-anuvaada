# Sutra प.5.1.66: दण्डादिभ्यः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — daRqAdiByaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.66"
SUTRA_TEXT = "दण्डादिभ्यः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — daRqAdiByaH"


class Sutra5166:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.66: अग्निः'),
		('रामः', '', 'प.5.1.66: रामः'),
		('सीता', '', 'प.5.1.66: सीता'),
	]

