# Sutra प.5.3.51: मानपश्वङ्गयोः कन्लुकौ च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — mAnapaSvaNgayoH kanlukO ca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.51"
SUTRA_TEXT = "मानपश्वङ्गयोः कन्लुकौ च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — mAnapaSvaNgayoH kanlukO ca"


class Sutra5351:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.51: अग्निः'),
		('रामः', '', 'प.5.3.51: रामः'),
		('सीता', '', 'प.5.3.51: सीता'),
	]

