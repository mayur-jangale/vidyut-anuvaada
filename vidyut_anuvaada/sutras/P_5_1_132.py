# Sutra प.5.1.132: योपधाद्गुरूपोत्तमाद्वुञ्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — yopaDAdgurUpottamAdvuY

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.132"
SUTRA_TEXT = "योपधाद्गुरूपोत्तमाद्वुञ्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — yopaDAdgurUpottamAdvuY"


class Sutra51132:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.132: अग्निः'),
		('रामः', '', 'प.5.1.132: रामः'),
		('सीता', '', 'प.5.1.132: सीता'),
	]

