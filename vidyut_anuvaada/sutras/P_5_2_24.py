# Sutra प.5.2.24: तस्य पाकमूले पील्वादिकर्णादिभ्यः कुणब्जाहचौ
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — tasya pAkamUle pIlvAdikarRAdiByaH kuRabjAhacO

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.24"
SUTRA_TEXT = "तस्य पाकमूले पील्वादिकर्णादिभ्यः कुणब्जाहचौ"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — tasya pAkamUle pIlvAdikarRAdiByaH kuRabjAhacO"


class Sutra5224:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.24: अग्निः'),
		('रामः', '', 'प.5.2.24: रामः'),
		('सीता', '', 'प.5.2.24: सीता'),
	]

