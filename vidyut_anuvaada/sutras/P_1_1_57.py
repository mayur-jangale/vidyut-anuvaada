# Sutra प.1.1.57: अचः परस्मिन् पूर्वविधौ
# (Samjna (technical definitions)) — acaH parasmin pUrvaviDO

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.57"
SUTRA_TEXT = "अचः परस्मिन् पूर्वविधौ"
SUTRA_DESC = "(Samjna (technical definitions)) — acaH parasmin pUrvaviDO"


class Sutra1157:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_57
		return apply_1_1_57(word, pos)

	EXAMPLES = [
		('अचः', '', 'प.1.1.57:acaḥ-parasmin-pUrvaviDHau;input=अचः'),
		('अग्नि', '', 'प.1.1.57:acaḥ-parasmin-pUrvaviDHau;input=अग्नि'),
	]

