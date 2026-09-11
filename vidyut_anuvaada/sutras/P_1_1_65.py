# Sutra प.1.1.65: अलोऽन्त्यात् पूर्व उपधा
# (Samjna (technical definitions)) — alo'ntyAt pUrva upaDA

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.65"
SUTRA_TEXT = "अलोऽन्त्यात् पूर्व उपधा"
SUTRA_DESC = "(Samjna (technical definitions)) — alo'ntyAt pUrva upaDA"


class Sutra1165:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_65
		return apply_1_1_65(word, pos)

	EXAMPLES = [
		('अल', '', "प.1.1.65:alo'ntyāt-pūrva-upaDA;input=अल"),
		('अग्नि', '', "प.1.1.65:alo'ntyāt-pūrva-upaDA;input=अग्नि"),
	]

