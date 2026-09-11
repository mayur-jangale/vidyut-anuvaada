# Sutra प.2.4.32: इदमोऽन्वादेशेऽशनुदात्तस्तृतीयादौ
# (Samasa (compound formation)) — idamo'nvAdeSe'SanudAttastftIyAdO

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.32"
SUTRA_TEXT = "इदमोऽन्वादेशेऽशनुदात्तस्तृतीयादौ"
SUTRA_DESC = "(Samasa (compound formation)) — idamo'nvAdeSe'SanudAttastftIyAdO"


class Sutra2432:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

