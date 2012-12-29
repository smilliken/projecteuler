main = print . maximum . filter isPalindrome $ [x * y | x <- [100..999], y <- [100..x]]
isPalindrome = (\x -> x == reverse x) . show