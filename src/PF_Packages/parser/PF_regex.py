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
        [.]?        # decimal (may or may not have 1 decimal point)
        [\d]*       # fractional part (may or may not have this part)
        """, regex.VERBOSE)
    # Pattern to match a positive number, can be a decimal number
    # Does include 0 

    @classmethod
    def match_two_nums(cls, data: str) -> bool:
        """Returns True if data has only 2 numbers in it.
        Otherwise False."""
        numbers: List[str] = cls.non_neg_num_pattern.findall(data)

        if len(numbers) == 2:
            # This means only found 2 numbers, which is what we expect
            return True
        else:
            return False
    
    @classmethod
    def match_one_non_zero_num(cls, data: str) -> bool:
        """Returns True if data has only 1 non-zero number in it.
        Otherwise False. 
        """
        numbers: List[str] = cls.non_neg_num_pattern.findall(data)
        
        if len(numbers) == 1:
            # This means only found 1 number, which is what we expect
            # Now we check if number is 0 or not, as pattern only matchs non-negative numbers
            if float(numbers[0]) != 0:
                # if will filter out any 0 to not return True 
                return True

        return False

    @classmethod
    def find_all_nums(cls, data: str) -> List[float]:
        """Find all the numbers within data, then returns then all in a list, in order of finding them.
        This will filter out anything that isn't a number (the decimal point will be included).
        This also means any negative numbers will have their '-' ignored, thus returned as a positive number."""

        numbers: List[float] = []

        for match_num in cls.non_neg_num_pattern.finditer(data):
            num: str = match_num.group()
            numbers.append(float(num))
        
        return numbers
