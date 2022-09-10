from dictionary import letter_dict


class Convert:

    # Convertor Function

    def convert(self, text):
        morse_str = ""
        for letter in text:
            if letter in letter_dict:
                morse_str += letter_dict[letter]
                morse_str += " "
            else:
                # For unadmitted characters
                morse_str += "*?*"

        return morse_str
