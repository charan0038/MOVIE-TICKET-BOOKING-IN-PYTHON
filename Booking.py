import mysql.connector 
import datetime
import smtplib
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="moviebookingdb"
)
mycursor=mydb.cursor()

def book_ticket(movie_name, customer_name, seats, show_time):
    sql = "INSERT INTO Bookings (movie_name, customer_name, seats, show_time) VALUES (%s, %s, %s, %s)"
    values = (movie_name, customer_name, seats, show_time)
    mycursor.execute(sql, values)
    mydb.commit()
    print(f"Booking confirmed for {customer_name} for movie {movie_name}.")

def send_email():
    try:
        Gmail = input("Enter your Gmail:")
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("2kcharan@gmail.com", "mrto bqhz rkkz ajpe")  
        message = "Your ticket has been booked successfully"
        s.sendmail("2kcharan@gmail.com", Gmail, message)
        s.quit()
        print("Mail sent successfully")
    except :
        print(f"Your mail was not sent !")

def view_bookings():
    mycursor.execute("SELECT * FROM Bookings")
    result = mycursor.fetchall()
    for booking in result:
        print(booking)

def main():
        print("\n Welcome To 2K Cinemas")
        print("\n Movie Ticaket Booking ")
        print("1. Book a Movie")
        print("2. View All Bookings")
        print("3. Exit")
        choice =input("Enter your chice:")
        if choice == '1':
            print("Available Movies are =[Garudan,HitList,MahaRaja]")
            movie_name = input("Enter your movie name:")
            if movie_name == "Garudan":
                print(f"Yes! {movie_name} is available")
                customer_name = input("Enter customer name:")
                seats = input("Enter number of seats:") 
                print ("show times formate['YYYY/MM/DD','HH:MM:SS']")
                show_time = input("Enter show time:")
                T=datetime.datetime.now()
                print(f"you Booked movie on this time {T} ")
                book_ticket(movie_name, customer_name, seats, show_time)
                send_email()

            elif movie_name == "HitList":
                 print(f"Yes! {movie_name} is available")
                 customer_name = input("Enter customer name:")
                 seats = input("Enter number of seats:") 
                 print ("Available show times['07:00:00 AM','10:30:00 AM','02:00:00 PM','05:00:00 PM','10:00:00 PM']")
                 print("show Time formate are [YYYY/MM/DD, 'HH:MM:SS']")
                 show_time = input("Enter show time:")
                 T=datetime.datetime.now()
                 print(f"you Booked movie on this time {T} ")
                 book_ticket(movie_name, customer_name, seats, show_time)
                 send_email()

            elif movie_name == "MahaRaja":
                 print(f"Yes! {movie_name} is available")
                 customer_name = input("Enter customer name:")
                 seats = input("Enter number of seats:") 
                 print ("Available show times['07:00:00 AM','10:30:00 AM','02:00:00 PM','05:00:00 PM','10:00:00 PM']")
                 show_time = input("Enter show time:")
                 T=datetime.datetime.now()
                 print(f"you Booked movie on this time {T} ")
                 book_ticket(movie_name, customer_name, seats, show_time)
                 send_email()
            else:
                print(f"This movie '{movie_name}' is unavailable")
        elif choice=='2':
             view_bookings()

        elif choice =='3':
             print("Exit....")

        else:
             print("Enter your correct choice !")



main() 
mycursor.close()
mydb.close()