# Sutra प.5.4.80: श्वसो वसीयःश्रेयसः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — Svaso vasIyaHSreyasaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.80"
SUTRA_TEXT = "श्वसो वसीयःश्रेयसः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — Svaso vasIyaHSreyasaH"


class Sutra5480:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.80: अग्निः'),
		('रामः', '', 'प.5.4.80: रामः'),
		('सीता', '', 'प.5.4.80: सीता'),
	]

