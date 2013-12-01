import Data.Word
import qualified Data.List.Stream as S

collatzLen :: Word32 -> Int
collatzLen a0 =
  let collatz n = (if even n then n else 3 * n + 1) `div` 2
  in  S.length $ S.takeWhile (/= 1) $ S.iterate collatz a0

main = print . snd . S.maximum . S.map (\ x -> (collatzLen x, x)) $ [1..1000000]
