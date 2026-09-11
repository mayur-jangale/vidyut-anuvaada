# Sutra प.7.2.18: क्षुब्धस्वान्तध्वान्तलग्नम्लिष्टविरिब्धफाण्टबाढानि मन्थमनस्तमःसक्ताविस्पष्टस्वरानायासभृशेषु
# (Taddhita (secondary derivations)) — kzubDasvAntaDvAntalagnamlizwaviribDaPARwabAQAni manTamanastamaHsaktAvispazwasvarAnAyAsaBfSezu

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.18"
SUTRA_TEXT = "क्षुब्धस्वान्तध्वान्तलग्नम्लिष्टविरिब्धफाण्टबाढानि मन्थमनस्तमःसक्ताविस्पष्टस्वरानायासभृशेषु"
SUTRA_DESC = "(Taddhita (secondary derivations)) — kzubDasvAntaDvAntalagnamlizwaviribDaPARwabAQAni manTamanastamaHsaktAvispazwasvarAnAyAsaBfSezu"


class Sutra7218:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.18: अग्निः'),
		('रामः', '', 'प.7.2.18: रामः'),
		('सीता', '', 'प.7.2.18: सीता'),
	]

