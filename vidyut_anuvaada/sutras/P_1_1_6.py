# Sutra प.1.1.6: दीधीवेवीटाम्
# Dīdhīvevīṭām — the roots धीधी, वेवी, and ईट् are special

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.6"
SUTRA_TEXT = "दीधीवेवीटाम्"
SUTRA_DESC = "Dīdhīvevīṭām — the roots धीधी, वेवी, and ईट् are special"


class Sutra116:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_6
		return apply_1_1_6(word, pos)

	EXAMPLES = [
		('धीधी', '', 'special-root:धीधी'),
		('वेवी', '', 'special-root:वेवी'),
		('पच', '', 'regular:पच'),
	]

