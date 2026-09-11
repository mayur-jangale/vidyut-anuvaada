# Sutra प.5.1.38: तस्य निमित्तं संयोगोत्पातौ
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — tasya nimittaM saMyogotpAtO

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.38"
SUTRA_TEXT = "तस्य निमित्तं संयोगोत्पातौ"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — tasya nimittaM saMyogotpAtO"


class Sutra5138:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.38: अग्निः'),
		('रामः', '', 'प.5.1.38: रामः'),
		('सीता', '', 'प.5.1.38: सीता'),
	]

