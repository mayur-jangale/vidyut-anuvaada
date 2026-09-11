# Sutra प.5.1.72: पारायणतुरायणचान्द्रायणं वर्तयति
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — pArAyaRaturAyaRacAndrAyaRaM vartayati

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.72"
SUTRA_TEXT = "पारायणतुरायणचान्द्रायणं वर्तयति"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — pArAyaRaturAyaRacAndrAyaRaM vartayati"


class Sutra5172:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.72: अग्निः'),
		('रामः', '', 'प.5.1.72: रामः'),
		('सीता', '', 'प.5.1.72: सीता'),
	]

