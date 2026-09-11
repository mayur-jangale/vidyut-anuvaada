# Sutra प.5.4.90: उत्तमैकाभ्यां च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — uttamEkAByAM ca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.90"
SUTRA_TEXT = "उत्तमैकाभ्यां च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — uttamEkAByAM ca"


class Sutra5490:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.90: अग्निः'),
		('रामः', '', 'प.5.4.90: रामः'),
		('सीता', '', 'प.5.4.90: सीता'),
	]

