# import part6functions as fx
# import stuff.part6functions as blah
import stuff
import pyodbc as dbconn

with dbconn.connect("Login Prompt=False;User ID=root;Password=root;Data Source=localhost:3306;Database=company;CHARSET=UTF8") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM country")


#stuff.stuffFx1.someFx()


# blah.somethingElse()
# blah.doSomething()

# fx.somethingElse()
# fx.main()