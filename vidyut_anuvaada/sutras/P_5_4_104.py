# Sutra प.5.4.104: ब्रह्मणो जानपदाख्यायाम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — brahmaRo jAnapadAKyAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.104"
SUTRA_TEXT = "ब्रह्मणो जानपदाख्यायाम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — brahmaRo jAnapadAKyAyAm"


class Sutra54104:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.104: अग्निः'),
		('रामः', '', 'प.5.4.104: रामः'),
		('सीता', '', 'प.5.4.104: सीता'),
	]

