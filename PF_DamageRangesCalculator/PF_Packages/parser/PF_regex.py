import regex
from typing import TypeAlias, List

Pattern: TypeAlias = regex.Pattern

class PF_Regex:
    """Class that handles all regex patterns and 
    matching for this app.
    """
    non_neg_num_pattern: Pattern = regex.compile(
        r"""        # First try to match a decimal
        [\d]+       # integer part     
        [.]         # decimal
        [\d]+       # fractional part
        |           # now check for only whole number as the decimal match failed
        [\d]+       # just digits
        """, regex.VERBOSE)
    # Pattern to match a positive number, can be a decimal number
    # Does include 0 

    @classmethod
    def match_two_non_neg_nums(cls, data: str) -> bool:
        """Returns True if data has only 2 non-negative numbers in it.
        Otherwise False."""
        numbers: List[str] = cls.non_neg_num_pattern.findall(data)

        if len(numbers) == 2:
            # This means only found 2 numbers, which is what we expect
            return True
        else:
            return False
    
    @classmethod
    def match_one_pos_num(cls, data: str) -> bool:
        """Returns True if data has only 1 positive number in it.
        Otherwise False."""
        numbers: List[str] = cls.non_neg_num_pattern.findall(data)
        
        if len(numbers) == 1:
            # This means only found 1 number, which is what we expect
            # Now we check if number is 0 or not, as pattern only matchs non-negative numbers
            if float(numbers[0]) != 0:
                # if will filter out any 0 to not return True 
                return True

        return False