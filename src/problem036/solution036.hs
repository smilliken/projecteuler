import Data.Char (intToDigit)
import Numeric (showIntAtBase)
main = print . sum . filter (isPalindrome 2) . filter (isPalindrome 10) $
       [1..999999]
isPalindrome base x = x' == reverse x'
    where x' = showIntAtBase base intToDigit x ""
