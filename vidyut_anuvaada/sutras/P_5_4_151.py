# Sutra प.5.4.151: उरःप्रभृतिभ्यः कप्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — uraHpraBftiByaH kap

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.151"
SUTRA_TEXT = "उरःप्रभृतिभ्यः कप्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — uraHpraBftiByaH kap"


class Sutra54151:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.151: अग्निः'),
		('रामः', '', 'प.5.4.151: रामः'),
		('सीता', '', 'प.5.4.151: सीता'),
	]

