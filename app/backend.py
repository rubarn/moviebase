
def main_menu():
    print("0: quit")
    print("1. title")
    print("2. actor")

    while True:
        try:
            choice = int(input("Choose 0, 1, or 2): "))
            if choice in [0, 1, 2]:
                return choice
            else:
                print("Invalid")
        except ValueError:
            print("Invalid")

def get_movie_input():
    title = input("Enter title: ")
    year = input("Enter year of release: ")
    year2 = year
    return title.strip(), year.strip(), year2.strip()

def get_actor_input():
    actor_name = input("Enter name of actor: ")
    return actor_name.strip()

def recommend_by_movie(conn, title, year, year2):
    try:
        cursor = conn.cursor()
        query = f"""
        SELECT DISTINCT tb.primaryTitle, tb.startYear
        FROM [title.basics] tb
        JOIN [title.principals] tp ON tb.titleID = tp.titleID
        JOIN [name.basics] nb ON tp.nameID = nb.nameID
        WHERE nb.nameID IN (
            SELECT DISTINCT tp2.nameID
            FROM [title.principals] tp2
            JOIN [title.basics] tb2 ON tp2.titleID = tb2.titleID
            WHERE tb2.primaryTitle = ?
            AND tb2.startYear = ?
        )
        AND tb.primaryTitle != ?
        AND tb.titleType = 'movie'
        ORDER BY tb.startYear DESC;
        """
        cursor.execute(query, (title, year, year2))
        recommendations = cursor.fetchall()

        if recommendations:
            print("Based on ", title, "(", year, "): ")
            for rec in recommendations:
                print(f"- {rec[0]} ({rec[1]})")
        else:
            print("No findings")
    except Exception as e:
        print("Failed: ", e)

def recommend_by_actor(conn, actor_name):
    try:
        cursor = conn.cursor()
        query = f"""
        SELECT DISTINCT tb.primaryTitle, tb.startYear
        FROM [name.basics] nb
        JOIN [title.principals] tp ON nb.nameID = tp.nameID
        JOIN [title.basics] tb ON tp.titleID = tb.titleID
        WHERE nb.primaryName = ?
        ORDER BY tb.startYear DESC;
        """
        cursor.execute(query, (actor_name,))
        recommendations = cursor.fetchall()

        if recommendations:
            print("Vi anbefaler disse filmene basert på skuespilleren", actor_name, ":")
            for rec in recommendations:
                print(f"- {rec[0]} ({rec[1]})")
        else:
            print("Ingen anbefalinger funnet for denne skuespilleren.")
    except Exception as e:
        print("Feil ved henting av anbefalinger:", e)
