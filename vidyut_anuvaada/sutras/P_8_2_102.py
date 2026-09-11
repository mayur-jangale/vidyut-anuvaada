# Sutra प.8.2.102: उपरिस्विदासीदिति च
# (Final transformations (tripāḍī)) — uparisvidAsIditi ca

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.102"
SUTRA_TEXT = "उपरिस्विदासीदिति च"
SUTRA_DESC = "(Final transformations (tripāḍī)) — uparisvidAsIditi ca"


class Sutra82102:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.102: अग्निः'),
		('रामः', '', 'प.8.2.102: रामः'),
		('सीता', '', 'प.8.2.102: सीता'),
	]

