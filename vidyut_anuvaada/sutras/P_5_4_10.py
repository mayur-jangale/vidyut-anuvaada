# Sutra प.5.4.10: स्थानान्ताद्विभाषा सस्थानेनेति चेत्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — sTAnAntAdviBAzA sasTAneneti cet

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.10"
SUTRA_TEXT = "स्थानान्ताद्विभाषा सस्थानेनेति चेत्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — sTAnAntAdviBAzA sasTAneneti cet"


class Sutra5410:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.10: अग्निः'),
		('रामः', '', 'प.5.4.10: रामः'),
		('सीता', '', 'प.5.4.10: सीता'),
	]

