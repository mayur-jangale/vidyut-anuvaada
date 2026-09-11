# Sutra प.5.4.87: अहस्सर्वैकदेशसंख्यातपुण्याच्च रात्रेः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — ahassarvEkadeSasaMKyAtapuRyAcca rAtreH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.87"
SUTRA_TEXT = "अहस्सर्वैकदेशसंख्यातपुण्याच्च रात्रेः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — ahassarvEkadeSasaMKyAtapuRyAcca rAtreH"


class Sutra5487:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.87: अग्निः'),
		('रामः', '', 'प.5.4.87: रामः'),
		('सीता', '', 'प.5.4.87: सीता'),
	]

