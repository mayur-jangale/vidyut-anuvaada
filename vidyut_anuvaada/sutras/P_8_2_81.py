# Sutra प.8.2.81: एत ईद्बहुवचने
# (Final transformations (tripāḍī)) — eta Idbahuvacane

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.81"
SUTRA_TEXT = "एत ईद्बहुवचने"
SUTRA_DESC = "(Final transformations (tripāḍī)) — eta Idbahuvacane"


class Sutra8281:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.81: अग्निः'),
		('रामः', '', 'प.8.2.81: रामः'),
		('सीता', '', 'प.8.2.81: सीता'),
	]

