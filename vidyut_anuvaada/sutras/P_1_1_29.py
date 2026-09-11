# Sutra प.1.1.29: न बहुव्रीहौ
# (Samjna (technical definitions)) — na bahuvrIhO

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.29"
SUTRA_TEXT = "न बहुव्रीहौ"
SUTRA_DESC = "(Samjna (technical definitions)) — na bahuvrIhO"


class Sutra1129:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_29
		return apply_1_1_29(word, pos)

	EXAMPLES = [
		('देव', 'bahuvrihi', 'bahuvrihi-suppresses:देव'),
		('देव', '', 'rule-applies:देव'),
	]

