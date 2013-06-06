-module(solution036).
-export([start/0]).

start() ->
    io:format("~p\n", [lists:foldl(fun(X, Y) -> X + Y end, 0,
        lists:filter(fun(X) ->
                isPalindrome("~.2B", X) and isPalindrome("~.10B", X) end,
            lists:seq(1, 1000000)))]).

isPalindrome(FormatStr, Num) ->
    NumStr = hd(io_lib:format(FormatStr, [Num])),
    (NumStr == lists:reverse(NumStr)).
