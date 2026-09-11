# Sutra प.5.2.100: लोमादिपामादिपिच्छादिभ्यः शनेलचः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — lomAdipAmAdipicCAdiByaH SanelacaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.100"
SUTRA_TEXT = "लोमादिपामादिपिच्छादिभ्यः शनेलचः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — lomAdipAmAdipicCAdiByaH SanelacaH"


class Sutra52100:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.100: अग्निः'),
		('रामः', '', 'प.5.2.100: रामः'),
		('सीता', '', 'प.5.2.100: सीता'),
	]

