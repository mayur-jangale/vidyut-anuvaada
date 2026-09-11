# Sutra प.5.4.78: ब्रह्महस्तिभ्याम् वर्च्चसः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — brahmahastiByAm varccasaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.78"
SUTRA_TEXT = "ब्रह्महस्तिभ्याम् वर्च्चसः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — brahmahastiByAm varccasaH"


class Sutra5478:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.78: अग्निः'),
		('रामः', '', 'प.5.4.78: रामः'),
		('सीता', '', 'प.5.4.78: सीता'),
	]

