# Sutra प.5.2.111: काण्डाण्डादीरन्नीरचौ
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — kARqARqAdIrannIracO

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.111"
SUTRA_TEXT = "काण्डाण्डादीरन्नीरचौ"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — kARqARqAdIrannIracO"


class Sutra52111:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.111: अग्निः'),
		('रामः', '', 'प.5.2.111: रामः'),
		('सीता', '', 'प.5.2.111: सीता'),
	]

