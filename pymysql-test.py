import pymysql
  
conn = pymysql.connect(
        host="integration-fulfillment-api-aurora-mysql-inst1.cro1np9fiity.us-east-1.rds.amazonaws.com",
        user="orgpdata_app_ro1",
        password = "Reusable_00JudginglyMammal",
        db="information_schema"
        )