from db_conn import connect_to_db
from backend import *

#Main method/UI
def main():
    conn = connect_to_db()

    if not conn:
        print("Failed")
        return

    try:
        while True:
            choice = main_menu()
            if choice == 0:
                break
            if choice == 1:
                title, year, year2 = get_movie_input()
                recommend_by_movie(conn, title, year, year2)
            elif choice == 2:
                actor_name = get_actor_input()
                recommend_by_actor(conn, actor_name)

            print("\n")
    finally:
        conn.close()
        print("Closed.")

main()
