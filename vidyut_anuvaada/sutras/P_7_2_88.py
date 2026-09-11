# Sutra प.7.2.88: प्रथमायाश्च द्विवचने भाषायाम्
# (Taddhita (secondary derivations)) — praTamAyASca dvivacane BAzAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.88"
SUTRA_TEXT = "प्रथमायाश्च द्विवचने भाषायाम्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — praTamAyASca dvivacane BAzAyAm"


class Sutra7288:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.88: अग्निः'),
		('रामः', '', 'प.7.2.88: रामः'),
		('सीता', '', 'प.7.2.88: सीता'),
	]

