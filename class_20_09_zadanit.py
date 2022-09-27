#  ПРИМЕР №1

class BankDate:
	counter = 0
	def __init__(self, name1, name2, name3, birthday, phonNumber, sity, country):
		BankDate.counter += 1
		self.name1 = name1
		self.name2 = name2
		self.name3 = name3
		self.birthday = birthday
		self.phonNumber = phonNumber
		self.sity = sity
		self.country = country
		
	def printCounter(self):
		print(self)
	
	
	def print_date(self):
		print(self.name1, self.name2, self.name3, self.birthday, self.phonNumber, self.sity, self.country)
	
	def date(self):
		return
	
if __name__ == "__main__":
    user1 = BankDate('Ivanov', 'Ivan', 'Ivanovich', "11.11.2011", '+10 950 05 11', 'Pscov', 'Russia')
    user2 = BankDate('Petrov', 'Petr', 'Petrovich', "10.01.1995", '+18 895 55 12', 'Kursk', 'Russia')
    user3 = BankDate('Petrov', 'Petr', 'Petrovich', "10.01.1995", '+18 895 55 12', 'Kursk', 'Russia')
    
    print(user1.name1)
    print(user2.name2)
    print(user1.name3)
    print(user2.birthday)
    print(user1.phonNumber)
    print(user2.sity)
    print(user1.country)


