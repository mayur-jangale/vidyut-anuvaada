# Sutra प.1.1.69: अणुदित् सवर्णस्य चाप्रत्ययः
# (Samjna (technical definitions)) — aRudit savarRasya cApratyayaH

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.69"
SUTRA_TEXT = "अणुदित् सवर्णस्य चाप्रत्ययः"
SUTRA_DESC = "(Samjna (technical definitions)) — aRudit savarRasya cApratyayaH"


class Sutra1169:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_69
		return apply_1_1_69(word, pos)

	EXAMPLES = [
		('अणु', '', 'प.1.1.69:aṇudit-savarṇasya-cāpratyayaḥ;input=अणु'),
		('अग्नि', '', 'प.1.1.69:aṇudit-savarṇasya-cāpratyayaḥ;input=अग्नि'),
	]

