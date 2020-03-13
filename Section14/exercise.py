import mysql.connector

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()

#word = input("Enter a Word: ")

query = cursor.execute("SELECT * FROM Dictionary WHERE length(Expression) < 2")
results = cursor.fetchall()

if results:
    for result in results:
        print(result)
else:
    print(results)
    print("No results found!")