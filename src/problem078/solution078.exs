defmodule Partitions do
    def pentagonal(n) do
        div(n * (3 * n - 1), 2)
    end
    def generalized_pentagonal(n) do
        k = div(n, 2) + 1
        pentagonal((if rem(n, 2) == 0 do 1 else -1 end) * k)
    end
    def partitions(n, memo) do
        (if HashDict.has_key?(memo, n) do HashDict.get(memo, n) else (
            case n do
                x when x < 0 -> 0
                0 -> 1
                1 -> 1
                _ -> Stream.iterate(0, &(&1+1)) |>
                     Stream.map(&(if rem(&1, 4) > 1 do -1 else 1 end) * partitions(n - generalized_pentagonal(&1), memo)) |>
                     Stream.take_while(&(&1 != 0)) |>
                     Enum.sum()
        end) end)
    end
end

IO.puts Stream.iterate(0, &(&1+1)) |>
    Stream.scan({nil, nil,  HashDict.new()}, fn (n, {_, _, memo}) ->
        p = Partitions.partitions(n, memo); {n, p, HashDict.put(memo, n, p)} end) |>
    Stream.drop_while(fn {_, p, _} -> rem(p, 1000000) > 0 end) |>
    Stream.map(fn {n, _, _} -> n end) |>
    Enum.take(1) |> List.first()
