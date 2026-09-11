# Sutra प.5.4.94: अनोऽश्मायस्सरसाम् जातिसंज्ञयोः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — ano'SmAyassarasAm jAtisaMjYayoH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.94"
SUTRA_TEXT = "अनोऽश्मायस्सरसाम् जातिसंज्ञयोः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — ano'SmAyassarasAm jAtisaMjYayoH"


class Sutra5494:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.94: अग्निः'),
		('रामः', '', 'प.5.4.94: रामः'),
		('सीता', '', 'प.5.4.94: सीता'),
	]

