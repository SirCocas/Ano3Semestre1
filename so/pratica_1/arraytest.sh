a[1]=aaa
echo ${a[1]}
declare -a a[2]=bbb
a[4]=ddd
a[2+3]=eee
echo "List of elements"
echo ${a[*]}
echo "number of elements"
echo ${#a[*]}
echo "list of indices"
echo ${!a[*]}

echo "Printing every value"
for v in ${a[*]}
do
    echo $v
done

echo "Printing every value with the index associated"
for i in ${!a[*]}
do
    echo "a[$i] = ${a[$i]}"
done