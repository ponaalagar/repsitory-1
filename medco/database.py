import mysql.connector

conn_object=mysql.connector.connect(host="localhost", user="root",password="", database="mysql")
cur_object=conn_object.cursor()

query1='desc medco'
cur_object.execute(query1)
table=cur_object.fetchall()

def stockUpdate():
    medicine=input("enter the name of the medicine to update: ")
    quantity=int(input("enter the quantity of the medicine: "))
    cost=float(input("enter the cost of the medicine: "))
    disease=input("enter the disease for which the medicine is used: ")
    stock=int(input("enter the stock of the medicine: "))
    insert_query='INSERT INTO medco (medicineName,quantity,cost,disease,stock) VALUES (%s,%s,%s,%s,%s)'
    values=(medicine,quantity,cost,disease,stock)
    cur_object.execute(insert_query,values)
    conn_object.commit()

def showTable():
    query2='SELECT * FROM medco WHERE cost>15'
    cur_object.execute(query2)
    table=cur_object.fetchall()
    for row in table:
        print(row)

def delete():
    medicine = input("enter the name of the medicine to be deleted: ")
    query3 = 'DELETE FROM medco WHERE medicineName = %s'
    try:
        cur_object.execute(query3, (medicine,))
        conn_object.commit()
        print(f"Medicine '{medicine}' deleted successfully!")
    except mysql.connector.Error as err:
        print(f"Error deleting medicine: {err}")
def reduce_stock(medicine_name, quantity):
    # Get the current stock quantity from the database
    query = "SELECT stock FROM medco WHERE medicineName = %s"
    cur_object.execute(query, (medicine_name,))
    current_stock = cur_object.fetchone()[0]
    # Reduce the stock quantity by the specified amount
    new_stock = current_stock - quantity
    if(new_stock<0):
        print("insufficient stock")
        return -1
    # Update the stock quantity in the database
    query = "UPDATE medco SET stock = %s WHERE medicineName = %s"
    cur_object.execute(query, (new_stock, medicine_name))
    conn_object.commit()
    print(f"Stock of {medicine_name} reduced by {quantity} units. New stock: {new_stock}")


def bill():
    medicine=input("\nenter the name of the medicine: ")
    medicine=medicine.lower()
    query4='SELECT cost FROM medco WHERE medicineName = %s'
    cur_object.execute(query4,(medicine,))
    cost=cur_object.fetchone()
    if cost is not None:
        print("cost of the medicine is",cost[0])
    query5='SELECT disease FROM medco WHERE medicineName = %s'
    cur_object.execute(query5,(medicine,))
    disease=cur_object.fetchone()
    quantity=int(input('Enter quantity: '))
    flag=reduce_stock(medicine, quantity)
    if flag!=-1:
        c=float(cost[0])
        q=float(quantity)
        total=c*q*1.05
        print(f"\n\n    ----medco----\nmedicine: {medicine}\napplicable to:{disease[0]}\namount per medicine: {cost[0]}\ntotal amount with GST(5%): {total}")
    return 0

switcher = {
    1: lambda: bill(),
    2: lambda:stockUpdate(),
    3: lambda: showTable(),
    4: lambda: delete()
}

n = int(input('1:to print bill\n2:to update stock\n3:to view stock\n4:to delete in stock\nEnter you option: '))

result = switcher.get(n, lambda: print("Invalid option"))()
switcher.get(n,'default')

cur_object.close()
conn_object.close()

