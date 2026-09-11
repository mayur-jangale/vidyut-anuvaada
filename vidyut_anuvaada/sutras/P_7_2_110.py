# Sutra प.7.2.110: यः सौ
# (Taddhita (secondary derivations)) — yaH sO

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.110"
SUTRA_TEXT = "यः सौ"
SUTRA_DESC = "(Taddhita (secondary derivations)) — yaH sO"


class Sutra72110:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.110: अग्निः'),
		('रामः', '', 'प.7.2.110: रामः'),
		('सीता', '', 'प.7.2.110: सीता'),
	]

