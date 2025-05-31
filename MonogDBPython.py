import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = client['Employee']
empinfo = mydb.employeeinformation


record = {
    'firstname': 'John',
    'lastname': 'Doe',
    'department': 'HR',
    'Company': 'Facebook',
    'age': 25
}


record = [{
    'firstname': 'John',
    'lastname': 'Doe',
    'department': 'HR',
    'Company': 'Facebook',
    'age': 29
},
{
    'firstname': 'Apoorv',
    'lastname': 'Patidar',
    'department': 'Software Developer',
    'Company': 'Google'
},
{
    'firstname': 'Gojo',
    'lastname': 'Satoru',
    'department': 'Product Manager',
    'Company': 'Atlassian'
},
{
    'firstname': 'Sukuana',
    'lastname': 'Ryomen',
    'department': 'Manager',
    'Company': 'Microsoft'
}]
