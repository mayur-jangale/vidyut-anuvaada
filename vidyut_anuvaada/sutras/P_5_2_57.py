# Sutra प.5.2.57: नित्यं शतादिमासार्धमाससंवत्सराच्च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — nityaM SatAdimAsArDamAsasaMvatsarAcca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.57"
SUTRA_TEXT = "नित्यं शतादिमासार्धमाससंवत्सराच्च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — nityaM SatAdimAsArDamAsasaMvatsarAcca"


class Sutra5257:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.57: अग्निः'),
		('रामः', '', 'प.5.2.57: रामः'),
		('सीता', '', 'प.5.2.57: सीता'),
	]

