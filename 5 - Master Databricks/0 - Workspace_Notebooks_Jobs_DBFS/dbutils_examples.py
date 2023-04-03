# Databricks notebook source
dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

dbutils.jobs.help()

# COMMAND ----------

dbutils.fs.mkdirs("/tmp/folder_tmp")

# COMMAND ----------

dbutils.fs.put("/tmp/folder_tmp/hello.txt", "Hello, Databricks", True)

# COMMAND ----------

dbutils.fs.head("/tmp/folder_tmp/hello.txt")

# COMMAND ----------

dbutils.fs.mv("/tmp/folder_tmp/hello.txt", "/tmp/folder_tmp_2/hello.txt")

# COMMAND ----------

dbutils.fs.cp("/tmp/folder_tmp_2/hello.txt", "/tmp/folder_tmp/hello.txt")

# COMMAND ----------

dbutils.fs.rm("/tmp/folder_tmp_2/hello.txt")

# COMMAND ----------

dbutils.notebook.run("/Users/aniellequintao@hotmail.com/notebook",60)
