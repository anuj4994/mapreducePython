# mapreducePython
I have created map reduce code for the data set given in the data.csv file

It will generate how many times a vehicle type is in in the accident.

TO run it on cscloud use following commands

cd /usr/local/hadoop

hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input /users-cloud-16fs/shah2aj/in/nyc-traffic.csv -output /users-cloud-16fs/shah2aj/output/anuj4 -mapper mapper.py -reducer reducer.py -file ~/hw6/{mapper,reducer}.py
