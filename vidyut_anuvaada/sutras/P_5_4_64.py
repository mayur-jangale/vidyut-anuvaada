# Sutra प.5.4.64: दुःखात् प्रातिलोम्ये
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — duHKAt prAtilomye

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.64"
SUTRA_TEXT = "दुःखात् प्रातिलोम्ये"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — duHKAt prAtilomye"


class Sutra5464:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.64: अग्निः'),
		('रामः', '', 'प.5.4.64: रामः'),
		('सीता', '', 'प.5.4.64: सीता'),
	]

