#!/bin/bash

#!/bin/bash
# ex59.sh: Exercising functions (simple).
{ # This is about as simple as functions get.
echo "Analyizing the logs."
} # Function declaration must precede call.
fun ()
{ # A somewhat more complex function.
i=0
REPEATS=`cat ./apache_log.log | awk '{print $1}' | sort  -u`
echo
echo "And now the fun really begins."
echo
sleep $JUST_A_SECOND # Hey, wait a second!
while [ $i -lt $REPEATS ]
do
echo "----------FUNCTIONS---------->"
echo "<------------ARE-------------"
echo "<------------FUN------------>"
echo
let "i+=1"
done
}
# Now, call the functions.
funky
fun
exit $?
