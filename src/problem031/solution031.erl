-module(solution031).
-export([start/0]).

start() ->
    io:format("~p\n", [1 + length([1 ||
        P1 <- lists:seq(0, 200),
        P2 <- lists:seq(0, 100),
        P5 <- lists:seq(0, 40),
        P10 <- lists:seq(0, 20),
        P20 <- lists:seq(0, 10),
        P50 <- lists:seq(0, 4),
        P100 <- lists:seq(0, 2),
        ((P1 * 1 + P2 * 2 + P5 * 5 + P10 * 10 + P20 * 20 + P50 * 50 +
            P100 * 100) == 200)])]).
