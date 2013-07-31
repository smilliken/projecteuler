main = print . length .
    filter (\(_, _, day, dayOfWeek) -> (dayOfWeek == 1 && day == 1)) .
    takeWhile (\(year, _, _, _) -> year <= 2000) .
    dropWhile (\(year, _, _, _) -> year < 1901) .
    iterate increment $ (1900, 1, 1, 2)

daysInMonth year month
    | (month == 2 && year `mod` 4 == 0 &&
        (year `mod` 100 /= 0 || year `mod` 400 == 0)) = 29 -- leap year
    | otherwise =
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] !! (month - 1)

increment (year, month, day, dayOfWeek) =
    let day' = day `incmod` (daysInMonth year month)
        month' = if day' == 1 then month `incmod` 12 else month
        year' = if day' == 1 && month' == 1 then year + 1 else year
        in (year', month', day', dayOfWeek `incmod` 7)
    where incmod x d = x `mod` d + 1

