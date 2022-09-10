from dictionary import letter_dict


class Translate:

    # Translate Function

    def translate(self, code):
        code = code.split(" ")
        text = ""
        for letter in code:
            value = [i for i in letter_dict if letter_dict[i] == letter]
            if value:
                text += value[0]
        return text
