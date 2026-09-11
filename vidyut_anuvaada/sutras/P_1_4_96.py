# Sutra प.1.4.96: अपिः पदार्थसम्भावनान्ववसर्गगर्हासमुच्चयेषु
# (Samjna (technical definitions)) — apiH padArTasamBAvanAnvavasargagarhAsamuccayezu

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.96"
SUTRA_TEXT = "अपिः पदार्थसम्भावनान्ववसर्गगर्हासमुच्चयेषु"
SUTRA_DESC = "(Samjna (technical definitions)) — apiH padArTasamBAvanAnvavasargagarhAsamuccayezu"


class Sutra1496:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_96
		return apply_1_4_96(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-api-multi:अग्निः'),
		('रामः', '', 'not-api-multi:रामः'),
		('सीता', '', 'not-api-multi:सीता'),
	]

