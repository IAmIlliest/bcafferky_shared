# Databricks notebook source
# Unzip the file to a specified directory using the full path

%sh
unzip \
/Workspace/Repos/###REDACTED###/DataLakehouse/UnderstandingDeltaLogs.zip \
-d /Workspace/Repos/###REDACTED###/DataLakehouse

# COMMAND ----------

# Load the unzipped notebook

%run /Workspace/Repos/###REDACTED###/DataLakehouse/UnderstandingDeltaLogs/UnderstandingDeltaLogs.dbc
