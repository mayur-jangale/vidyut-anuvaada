# Sutra प.5.1.44: लोकसर्वलोकाट्ठञ्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — lokasarvalokAwWaY

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.44"
SUTRA_TEXT = "लोकसर्वलोकाट्ठञ्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — lokasarvalokAwWaY"


class Sutra5144:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.44: अग्निः'),
		('रामः', '', 'प.5.1.44: रामः'),
		('सीता', '', 'प.5.1.44: सीता'),
	]

