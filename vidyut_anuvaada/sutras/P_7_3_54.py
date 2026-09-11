# Sutra प.7.3.54: हो हन्तेर्ञ्णिन्नेषु
# (Taddhita (secondary derivations)) — ho hanterYRinnezu

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.54"
SUTRA_TEXT = "हो हन्तेर्ञ्णिन्नेषु"
SUTRA_DESC = "(Taddhita (secondary derivations)) — ho hanterYRinnezu"


class Sutra7354:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.54: अग्निः'),
		('रामः', '', 'प.7.3.54: रामः'),
		('सीता', '', 'प.7.3.54: सीता'),
	]

