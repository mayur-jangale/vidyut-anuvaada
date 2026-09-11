# Sutra प.5.3.92: किंयत्तदो निर्द्धारणे द्वयोरेकस्य डतरच्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — kiMyattado nirdDAraRe dvayorekasya qatarac

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.92"
SUTRA_TEXT = "किंयत्तदो निर्द्धारणे द्वयोरेकस्य डतरच्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — kiMyattado nirdDAraRe dvayorekasya qatarac"


class Sutra5392:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.92: अग्निः'),
		('रामः', '', 'प.5.3.92: रामः'),
		('सीता', '', 'प.5.3.92: सीता'),
	]

