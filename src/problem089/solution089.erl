-module(solution089).
-export([start/0]).

start() ->
    io:format("~p\n", [lists:foldl(fun(X, Y) -> X + Y end, 0,
        lists:map(fun(X) -> diffline(X) end, readFile("roman.txt")))]).

diffline(X) ->
    string:len(X) - string:len(toRoman(fromRoman(X))).

fromRoman(Str) ->
    Int1 = fromRomanChr(string:substr(Str, 1, 1)),
    Int2 = fromRomanChr(string:substr(Str, 2, 1)),
    Sign = if (Int1 < Int2) -> -1;
        true -> 1
    end,
    if (Int2 > 0) -> Sign * Int1 + fromRoman(string:substr(Str, 2));
        true -> Int1
    end.

fromRomanChr(Chr) ->
    if (Chr == "I") -> 1;
        (Chr == "V") -> 5;
        (Chr == "X") -> 10;
        (Chr == "L") -> 50;
        (Chr == "C") -> 100;
        (Chr == "D") -> 500;
        (Chr == "M") -> 1000;
        true -> 0
    end.

toRoman(N) ->
    if (N >= 1000) -> "M" ++ toRoman(N - 1000);
        (N >= 900) -> "CM" ++ toRoman(N - 900);
        (N >= 500) -> "D" ++ toRoman(N - 500);
        (N >= 400) -> "CD" ++ toRoman(N - 400);
        (N >= 100) -> "C" ++ toRoman(N - 100);
        (N >= 90) -> "XC" ++ toRoman(N - 90);
        (N >= 50) -> "L" ++ toRoman(N - 50);
        (N >= 40) -> "XL" ++ toRoman(N - 40);
        (N >= 10) -> "X" ++ toRoman(N - 10);
        (N >= 9) -> "IX" ++ toRoman(N - 9);
        (N >= 5) -> "V" ++ toRoman(N - 5);
        (N >= 4) -> "IV" ++ toRoman(N - 4);
        (N >= 1) -> "I" ++ toRoman(N - 1);
        true -> ""
    end.

readFile(FileName) ->
    {ok, Device} = file:open(FileName, [read]),
    try getLines(Device)
      after file:close(Device)
    end.

getLines(Device) ->
    case io:get_line(Device, "") of
        eof  -> [];
        Line -> [string:strip(Line, right, $\n)] ++ getLines(Device)
    end.
