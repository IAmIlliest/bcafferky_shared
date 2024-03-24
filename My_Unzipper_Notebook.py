# Databricks notebook source
# Unzip the file to a specified directory using the full path

%sh
unzip \
/Workspace/Repos/***REMOVED***/DataLakehouse/UnderstandingDeltaLogs.zip \
-d /Workspace/Repos/***REMOVED***/DataLakehouse

# COMMAND ----------

# Load the unzipped notebook

%run /Workspace/Repos/***REMOVED***/DataLakehouse/UnderstandingDeltaLogs/UnderstandingDeltaLogs.dbc
