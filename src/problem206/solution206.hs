main = print . head . filter (check . show . (^2)) $ [1010101010,1010101020..]
check ['1',_,'2',_,'3',_,'4',_,'5',_,'6',_,'7',_,'8',_,'9',_,'0'] = True
check _ = False
