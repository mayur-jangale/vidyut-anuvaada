# Sutra प.8.2.96: अङ्गयुक्तं तिङ् आकाङ्क्षम्
# (Final transformations (tripāḍī)) — aNgayuktaM tiN AkANkzam

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.96"
SUTRA_TEXT = "अङ्गयुक्तं तिङ् आकाङ्क्षम्"
SUTRA_DESC = "(Final transformations (tripāḍī)) — aNgayuktaM tiN AkANkzam"


class Sutra8296:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.96: अग्निः'),
		('रामः', '', 'प.8.2.96: रामः'),
		('सीता', '', 'प.8.2.96: सीता'),
	]

