# Sutra प.1.4.59: उपसर्गाः क्रियायोगे
# (Samjna (technical definitions)) — upasargAH kriyAyoge

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.59"
SUTRA_TEXT = "उपसर्गाः क्रियायोगे"
SUTRA_DESC = "(Samjna (technical definitions)) — upasargAH kriyAyoge"


class Sutra1459:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_59
		return apply_1_4_59(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-upasarga:अग्निः'),
		('रामः', '', 'not-upasarga:रामः'),
		('सीता', '', 'not-upasarga:सीता'),
	]

