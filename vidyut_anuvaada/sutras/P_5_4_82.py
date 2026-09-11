# Sutra प.5.4.82: प्रतेरुरसः सप्तमीस्थात्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — praterurasaH saptamIsTAt

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.82"
SUTRA_TEXT = "प्रतेरुरसः सप्तमीस्थात्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — praterurasaH saptamIsTAt"


class Sutra5482:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.82: अग्निः'),
		('रामः', '', 'प.5.4.82: रामः'),
		('सीता', '', 'प.5.4.82: सीता'),
	]

