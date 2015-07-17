defmodule Math do
  def factorial(n) do
    case n do
      0 -> 1
      m -> m * factorial(m - 1)
    end
  end
  def combinations(n, m) do
    factorial(n) / (factorial(m) * factorial(n - m))
  end
end

IO.puts length(for n <- 1..100, m <- 1..n, Math.combinations(n, m) > 1000000, do: 1)
