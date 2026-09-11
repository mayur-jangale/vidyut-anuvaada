# Sutra प.5.2.20: शालीनकौपीने अधृष्टाकार्ययोः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — SAlInakOpIne aDfzwAkAryayoH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.20"
SUTRA_TEXT = "शालीनकौपीने अधृष्टाकार्ययोः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — SAlInakOpIne aDfzwAkAryayoH"


class Sutra5220:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.20: अग्निः'),
		('रामः', '', 'प.5.2.20: रामः'),
		('सीता', '', 'प.5.2.20: सीता'),
	]

