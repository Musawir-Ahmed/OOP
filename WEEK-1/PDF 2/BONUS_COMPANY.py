# TSKING YEAR OF SERVICE FROM THE USER AS A INPUT
year_of_service = int(input("ENTER NUMBER OF YEAR OS SERVICE ="))
# COMPARING ACCORDING TO THE GIVEN CONDITIONS
if(year_of_service > 5):
    salary = float(input("ENTER YOUR SALARY ="))
    bonus = 0.05*salary
    salary = salary+bonus
    print("YOU GOT BONUS OF RS ", bonus)
    print("NOW YOUR SALARY IS RS ", salary)
else:
    print("YOU DID'NT GOT ANY BONUS")
