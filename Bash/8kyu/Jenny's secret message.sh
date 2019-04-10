Jenny's secret message
Python:
def greet(name):
    return "Hello, my love!" if name == "Johnny" else "Hello, {name}!".format(name=name)
11 months agoRefactorDiscuss
Shell:
#!/bin/bash

if [ "$1" == "Johnny" ]
then
echo "Hello. my Love!";
else
echo "Hello, $1!"
fi