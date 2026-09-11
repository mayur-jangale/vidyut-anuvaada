# Sutra प.5.4.122: नित्यमसिच् प्रजामेधयोः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — nityamasic prajAmeDayoH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.122"
SUTRA_TEXT = "नित्यमसिच् प्रजामेधयोः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — nityamasic prajAmeDayoH"


class Sutra54122:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.122: अग्निः'),
		('रामः', '', 'प.5.4.122: रामः'),
		('सीता', '', 'प.5.4.122: सीता'),
	]

