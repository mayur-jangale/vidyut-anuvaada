# Sutra प.8.2.100: अनुदात्तं प्रश्नान्ताभिपूजितयोः
# (Final transformations (tripāḍī)) — anudAttaM praSnAntABipUjitayoH

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.100"
SUTRA_TEXT = "अनुदात्तं प्रश्नान्ताभिपूजितयोः"
SUTRA_DESC = "(Final transformations (tripāḍī)) — anudAttaM praSnAntABipUjitayoH"


class Sutra82100:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.100: अग्निः'),
		('रामः', '', 'प.8.2.100: रामः'),
		('सीता', '', 'प.8.2.100: सीता'),
	]

