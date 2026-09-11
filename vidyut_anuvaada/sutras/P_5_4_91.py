# Sutra प.5.4.91: राजाहस्सखिभ्यष्टच्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — rAjAhassaKiByazwac

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.91"
SUTRA_TEXT = "राजाहस्सखिभ्यष्टच्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — rAjAhassaKiByazwac"


class Sutra5491:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.91: अग्निः'),
		('रामः', '', 'प.5.4.91: रामः'),
		('सीता', '', 'प.5.4.91: सीता'),
	]

