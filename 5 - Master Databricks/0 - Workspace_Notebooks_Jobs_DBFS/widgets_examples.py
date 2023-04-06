# Databricks notebook source
# DBTITLE 1,Text Widget
dbutils.widgets.text("TextWidget", "")

# COMMAND ----------

# DBTITLE 1,Dropdown Widget
dbutils.widgets.dropdown("DropdownWidget", "2", ["1", "2"])

# COMMAND ----------

# DBTITLE 1,Combo Widget
dbutils.widgets.combobox("ComboWidget", "US", ["US", "UK", "INDIA", "GERMAN"])

# COMMAND ----------

# DBTITLE 1,MultiSelect Widget
dbutils.widgets.multiselect("MultiSelectWidget", "US", ["CANADA", "US", "INDIA"])

# COMMAND ----------

# DBTITLE 1,Get Value
dbutils.widgets.get("MultiSelectWidget")


# COMMAND ----------

# DBTITLE 1,RemoveAll Widgets
dbutils.widgets.removeAll()

# COMMAND ----------

# DBTITLE 1,Create a dropdown widget of all databases in the current catalog:
dbutils.widgets.dropdown("database", "default", [database[0] for database in spark.catalog.listDatabases()])

# COMMAND ----------

# MAGIC %md
# MAGIC ##CREATE WIDGETS USING SQL

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE WIDGET TEXT TextWidget DEFAULT "NA"

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE WIDGET DROPDOWN DROPDOWN_WIDGET DEFAULT "1" CHOICES SELECT "1" UNION ALL SELECT "2"

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE WIDGET COMBOBOX COMBOBOX_WIDGET DEFAULT "1" CHOICES SELECT "1" UNION ALL SELECT "2"

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE WIDGET MULTISELECT MULTISELECT_WIDGET DEFAULT "1" CHOICES SELECT "1" UNION ALL SELECT "2"

# COMMAND ----------

# DBTITLE 1,Get Value
# MAGIC %sql
# MAGIC select getArgument("MULTISELECT_WIDGET")

# COMMAND ----------

# MAGIC %sql
# MAGIC remove widget MULTISELECT_WIDGET
