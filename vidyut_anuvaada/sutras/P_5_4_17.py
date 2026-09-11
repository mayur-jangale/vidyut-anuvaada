# Sutra प.5.4.17: संख्यायाः क्रियाभ्यावृत्तिगणने कृत्वसुच्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — saMKyAyAH kriyAByAvfttigaRane kftvasuc

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.17"
SUTRA_TEXT = "संख्यायाः क्रियाभ्यावृत्तिगणने कृत्वसुच्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — saMKyAyAH kriyAByAvfttigaRane kftvasuc"


class Sutra5417:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.17: अग्निः'),
		('रामः', '', 'प.5.4.17: रामः'),
		('सीता', '', 'प.5.4.17: सीता'),
	]

