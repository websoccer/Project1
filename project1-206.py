import os
import filecmp
'''from dateutil.relativedelta import *'''
from datetime import date


def getData(file):
        # get a list of dictionary objects from the file
        #Input: file name
        inFile = open(file, "r")
        lines = inFile.readlines()
        inFile.close()

#Ouput: return a list of dictionary objects where
#the keys are from the first row in the data. and the values are each of the other rows
        contact_List = []

        for line in lines[1:]:
                newDict = {}
                values = line.split(",")
                firstN = values[0]
                lastN = values[1]
                Email = values[2]
                Class = values[3]
                DOB = values[4]

                newDict["First"] = firstN
                newDict["Last"] = lastN
                newDict["Email"] = Email
                newDict["Class"] = Class
                newDict["DOB"] = DOB
                
                contact_List.append(newDict)
        
        return contact_List

def mySort(data,col):
# Sort based on key/column

        sortedList = sorted(data, key=lambda k: k[col])
        
#Input: list of dictionaries and col (key) to sort on
        
        firstN = sortedList[0]["First"]
        
        lastN = sortedList[0]["Last"]

#Output: Return the first item in the sorted list as a string of just: firstName lastName

        return firstN + " " + lastN

def classSizes(data):
# Create a histogram
# Input: list of dictionaries
        dataClassNumb = {}
        for values in data:
                if values["Class"] in dataClassNumb:
                        dataClassNumb[values["Class"]] += 1
                else:
                        dataClassNumb[values["Class"]] = 1
                        
        Lists = []
        for value in dataClassNumb:
                Lists.append((value, dataClassNumb[value]))
        # Output: Return a list of tuples sorted by the number of students in that class in
        # descending order
        # [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]
        return sorted(Lists, key = lambda k:k[1], reverse = True)


def findMonth(a):
# Find the most common birth month form this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data
        Month_Dictionary = {}

        for dictionary in a:
                day_of_birth = dictionary['DOB']
                m_d_y = day_of_birth.split("/")
                month = m_d_y[0]
                if month in Month_Dictionary:
                        Month_Dictionary[month] += 1
                else:
                        Month_Dictionary[month] = 1
        List_of_Month = []
        for months in Month_Dictionary:
                List_of_Month.append((int(months), Month_Dictionary[months]))
        m = sorted(List_of_Month, key = lambda k:k[1], reverse = True)
        return m[0][0]

def mySortPrint(a,col,fileName):
#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.

        sortedList = sorted(a, key=lambda k: k[col])

        mfile = open(fileName, "w")
        
        # as first,last,email
        #Input: list of dictionaries, col (key) to sort by and output file name
        for values in sortedList:
                values["First"]
                values["Last"]
                values["Email"]
                line = (values["First"] + ","+ values["Last"]+ ","+ values["Email"] + "\n")
                
#Output: No return value, but the file is written
                mfile.write(line)
                
        mfile.close()


def findAge(a):
# def findAge(a):
# Input: list of dictionaries
       student_ages = []
       for age_dictionary in a:
               values = age_dictionary["DOB"].split("/")
               month = int(values[0])
               day = int(values[1])
               year = int(values[2])

               student_ages.append(int(2018)-year)
       return round(sum(student_ages)/len(student_ages))

# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.

	



################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
