cur_object=conn_object.cursor()
query1='desc medco'
cur_object.execute(query1)
table=cur_object.fetchall()
for i in table:
    print(i)
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
    medicine=input("enter the name of the medicine to be deleted: ")
    query3 = 'DELETE FROM medco WHERE cost = %s'
    cur_object.execute(query3,medicine)
    conn_object.commit()
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
    medicine=input("enter the name of the medicine: ")
    medicine=medicine.lower()
    query4='SELECT cost FROM medco WHERE medicineName = %s'