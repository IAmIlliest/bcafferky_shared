# Databricks notebook source
# Unzip the file to a specified directory using the full path

quick twiddle 1 to nudge history for bfg testing
quick twiddle 2 to nudge history for bfg testing

%sh
unzip \
/Workspace/Repos/***REMOVED***/DataLakehouse/UnderstandingDeltaLogs.zip \
-d /Workspace/Repos/***REMOVED***/DataLakehouse

# COMMAND ----------

# Load the unzipped notebook

%run /Workspace/Repos/***REMOVED***/DataLakehouse/UnderstandingDeltaLogs/UnderstandingDeltaLogs.dbc
