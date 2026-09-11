# Sutra प.5.1.121: न नञ्पूर्वात्तत्पुरुषादचतुरसंगतलवणवटयुधकतरसलसेभ्यः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — na naYpUrvAttatpuruzAdacaturasaMgatalavaRavawayuDakatarasalaseByaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.121"
SUTRA_TEXT = "न नञ्पूर्वात्तत्पुरुषादचतुरसंगतलवणवटयुधकतरसलसेभ्यः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — na naYpUrvAttatpuruzAdacaturasaMgatalavaRavawayuDakatarasalaseByaH"


class Sutra51121:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.121: अग्निः'),
		('रामः', '', 'प.5.1.121: रामः'),
		('सीता', '', 'प.5.1.121: सीता'),
	]

