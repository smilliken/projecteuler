function fact {
    k=1
    for ((i=1; i<=$1; i++))
    do
        k=$[$k * $i]
    done
    echo $k
}

function check {
    sum=0
    for ((i=0; i<$(expr length $1); i++))
    do
        sum=$[$sum + $(fact ${1:$i:1})]
    done
    echo $(($sum==$1))
}

total=0
for ((i=3; i<41000; i++))
do
    if [ "$(check $i)" == "1" ]; then
        total=$[total + $i];
    fi
done
echo $total
