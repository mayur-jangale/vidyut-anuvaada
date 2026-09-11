# Sutra प.5.3.18: दानीं च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — dAnIM ca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.18"
SUTRA_TEXT = "दानीं च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — dAnIM ca"


class Sutra5318:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.18: अग्निः'),
		('रामः', '', 'प.5.3.18: रामः'),
		('सीता', '', 'प.5.3.18: सीता'),
	]

