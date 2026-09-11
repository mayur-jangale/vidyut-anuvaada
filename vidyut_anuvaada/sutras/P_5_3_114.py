# Sutra प.5.3.114: आयुधजीविसंघाञ्ञ्यड्वाहीकेष्वब्राह्मणराजन्यात्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — AyuDajIvisaMGAYYyaqvAhIkezvabrAhmaRarAjanyAt

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.114"
SUTRA_TEXT = "आयुधजीविसंघाञ्ञ्यड्वाहीकेष्वब्राह्मणराजन्यात्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — AyuDajIvisaMGAYYyaqvAhIkezvabrAhmaRarAjanyAt"


class Sutra53114:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.114: अग्निः'),
		('रामः', '', 'प.5.3.114: रामः'),
		('सीता', '', 'प.5.3.114: सीता'),
	]

