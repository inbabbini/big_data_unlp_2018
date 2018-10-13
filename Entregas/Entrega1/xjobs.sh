#!/usr/bin/env bash

# Move files to hdfs
echo "||---------------------Creating xjobs directory---------------------||"
hdfs dfs -mkdir xjobs

echo "||---------------------Copying datasets---------------------||"
hdfs dfs -copyFromLocal datasets xjobs/datasets

# Format data files
echo "||---------------------Formatting datasets---------------------||"
hdfs dfs -mkdir xjobs/fdatasets

hadoop jar ~/jarHadoop/hadoop-streaming-2.6.0.jar \
	-mapper "0_formatter/mapper.py A" \
	-file 0_formatter/mapper.py \
	-reducer 0_formatter/reducer.py \
	-file 0_formatter/reducer.py \
	-input xjobs/datasets/A.txt \
	-output xjobs/fdatasets/A

hadoop jar ~/jarHadoop/hadoop-streaming-2.6.0.jar \
	-mapper "0_formatter/mapper.py B" \
	-file 0_formatter/mapper.py \
	-reducer 0_formatter/reducer.py \
	-file 0_formatter/reducer.py \
	-input xjobs/datasets/B.txt \
	-output xjobs/fdatasets/B

hadoop jar ~/jarHadoop/hadoop-streaming-2.6.0.jar \
	-mapper "0_formatter/mapper.py C" \
	-file 0_formatter/mapper.py \
	-reducer 0_formatter/reducer.py \
	-file 0_formatter/reducer.py \
	-input xjobs/datasets/C.txt \
	-output xjobs/fdatasets/C

hadoop jar ~/jarHadoop/hadoop-streaming-2.6.0.jar \
	-mapper "0_formatter/mapper.py E" \
	-file 0_formatter/mapper.py \
	-reducer 0_formatter/reducer.py \
	-file 0_formatter/reducer.py \
	-input xjobs/datasets/E.txt \
	-output xjobs/felist


# Calculate X set
echo "||---------------------Calculate X set---------------------||"
hadoop jar ~/jarHadoop/hadoop-streaming-2.6.0.jar \
	-mapper 8_xset/mapper.py \
	-file 8_xset/mapper.py \
	-combiner 8_xset/combiner.py \
	-file 8_xset/combiner.py \
	-reducer 8_xset/reducer.py \
	-file 8_xset/reducer.py \
	-input xjobs/fdatasets/A \
	-input xjobs/fdatasets/B \
	-input xjobs/fdatasets/C \
	-output xjobs/xset


# Calculate X cardinality
echo "||---------------------Calculate X set cardinality---------------------||"
hadoop jar ~/jarHadoop/hadoop-streaming-2.6.0.jar \
	-mapper 5_cardinality/mapper.py \
	-file 5_cardinality/mapper.py \
	-combiner 5_cardinality/reducer.py \
	-file 5_cardinality/reducer.py \
	-reducer 5_cardinality/reducer.py \
	-file 5_cardinality/reducer.py \
	-input xjobs/xset \
	-output xjobs/xset_cardinality


# Calculate membership of E members in relationship to X
echo "||------------------Calculate membership of E list related to X set-----------------||"
hadoop jar ~/jarHadoop/hadoop-streaming-2.6.0.jar \
	-mapper 6_membership/mapper.py \
	-file 6_membership/mapper.py \
	-combiner 6_membership/combiner.py \
	-file 6_membership/combiner.py \
	-reducer 6_membership/reducer.py \
	-file 6_membership/reducer.py \
	-input xjobs/xset \
	-input xjobs/felist \
	-output xjobs/xset_membership