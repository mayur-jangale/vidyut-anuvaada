# Sutra प.4.2.96: कुलकुक्षिग्रीवाभ्यः श्वास्यलंकारेषु
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kulakukzigrIvAByaH SvAsyalaMkArezu

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.96"
SUTRA_TEXT = "कुलकुक्षिग्रीवाभ्यः श्वास्यलंकारेषु"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kulakukzigrIvAByaH SvAsyalaMkArezu"


class Sutra4296:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.96: अग्निः'),
		('रामः', '', 'प.4.2.96: रामः'),
		('सीता', '', 'प.4.2.96: सीता'),
	]

