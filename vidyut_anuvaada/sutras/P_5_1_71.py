# Sutra प.5.1.71: यज्ञर्त्विग्भ्यां घखञौ
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — yajYartvigByAM GaKaYO

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.71"
SUTRA_TEXT = "यज्ञर्त्विग्भ्यां घखञौ"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — yajYartvigByAM GaKaYO"


class Sutra5171:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.71: अग्निः'),
		('रामः', '', 'प.5.1.71: रामः'),
		('सीता', '', 'प.5.1.71: सीता'),
	]

