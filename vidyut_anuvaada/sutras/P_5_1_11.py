# Sutra प.5.1.11: माणवचरकाभ्यां खञ्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — mARavacarakAByAM KaY

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.11"
SUTRA_TEXT = "माणवचरकाभ्यां खञ्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — mARavacarakAByAM KaY"


class Sutra5111:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.11: अग्निः'),
		('रामः', '', 'प.5.1.11: रामः'),
		('सीता', '', 'प.5.1.11: सीता'),
	]

