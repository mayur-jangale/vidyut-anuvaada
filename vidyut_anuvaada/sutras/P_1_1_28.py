# Sutra प.1.1.28: विभाषा दिक्समासे बहुव्रीहौ
# (Samjna (technical definitions)) — viBAzA diksamAse bahuvrIhO

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.28"
SUTRA_TEXT = "विभाषा दिक्समासे बहुव्रीहौ"
SUTRA_DESC = "(Samjna (technical definitions)) — viBAzA diksamAse bahuvrIhO"


class Sutra1128:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_28
		return apply_1_1_28(word, pos)

	EXAMPLES = [
		('पूर्व', '', 'दिक्-first-member:पूर्व;optional-bahuvrihi'),
		('दक्षिण', '', 'दिक्-first-member:दक्षिण;optional-bahuvrihi'),
		('देव', '', 'non-dik:देव'),
	]

