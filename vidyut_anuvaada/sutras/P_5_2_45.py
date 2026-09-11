# Sutra प.5.2.45: तदस्मिन्नधिकमिति दशान्ताड्डः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — tadasminnaDikamiti daSAntAqqaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.45"
SUTRA_TEXT = "तदस्मिन्नधिकमिति दशान्ताड्डः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — tadasminnaDikamiti daSAntAqqaH"


class Sutra5245:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.45: अग्निः'),
		('रामः', '', 'प.5.2.45: रामः'),
		('सीता', '', 'प.5.2.45: सीता'),
	]

