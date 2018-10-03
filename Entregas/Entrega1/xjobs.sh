#!/usr/bin/env bash

# Move files to hdfs
hdfs dfs -mkdir xjobs

for file in /datasets/*; do
  hdfs dfs -copyFromLocal /datasets/$file xjobs/datasets/$file
done

# Format data files
hdfs dfs -mkdir xjobs/fdatasets

hadoop jar hadoop-streaming-2.6.0.jar 
	-mapper 0_formatter/mapper.py A 
	-reducer 0_formatter/reducer.py 
	-input xjobs/datasets/A.txt 
	-output xjobs/fdatasets

hadoop jar hadoop-streaming-2.6.0.jar 
	-mapper 0_formatter/mapper.py B 
	-reducer 0_formatter/reducer.py 
	-input xjobs/datasets/B.txt 
	-output xjobs/fdatasets

hadoop jar hadoop-streaming-2.6.0.jar 
	-mapper 0_formatter/mapper.py C 
	-reducer 0_formatter/reducer.py 
	-input xjobs/datasets/C.txt 
	-output xjobs/fdatasets

hadoop jar hadoop-streaming-2.6.0.jar 
	-mapper 0_formatter/mapper.py E 
	-reducer 0_formatter/reducer.py 
	-input xjobs/datasets/E.txt 
	-output xjobs/felist


# Calculate X set
hadoop jar hadoop-streaming-2.6.0.jar 
	-mapper 8_xset/mapper.py
	-reducer 8_xset/reducer.py 
	-input xjobs/datasets 
	-output xjobs/xset


# Calculate X cardinality
hadoop jar hadoop-streaming-2.6.0.jar 
	-mapper 5_cardinality/mapper.py
	-reducer 5_cardinality/reducer.py 
	-input xjobs/xset 
	-output xjobs/xset_cardinality


# Calculate membership of E members in relationship to X
hadoop jar hadoop-streaming-2.6.0.jar 
	-mapper 6_membership/mapper.py
	-reducer 6_membership/reducer.py 
	-input xjobs/xset
	-input xjobs/felist
	-output xjobs/xset_membership