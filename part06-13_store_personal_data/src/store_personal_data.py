# Write your solution here


def store_personal_data(person: tuple):
    #
    with open("people.csv", "a") as write_file:
        people = []

        for item in person:
            people.append(f"{item}")


        line = ";".join(people)
        write_file.write(line+"\n")
           


if __name__ == "__main__":
    person = ()
    person = (str("Paul Paulson"), int(37), float(175.5))
    store_personal_data(person)