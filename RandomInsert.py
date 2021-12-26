#!/usr/bin/python
# -*- coding: utf8 -*-
import random
import psycopg2


print('Enter database')
databaseName = str(input())
print('Enter user')
user = str(input())
print('Enter password')
password = input()
print('Enter host')
host = input()
print('Enter port')
port = int(input())

connect = psycopg2.connect(
    database=databaseName,
    user=user,
    password=password,
    host=host,
    port=port

)
print("Database opened succesfully")


def CreateTABLES():
    cur = connect.cursor()
    sql_file = open('table.sql', 'r')
    cur.execute(sql_file.read())

    print("Table created successfully")
    connect.commit()


def InsertTECHNOLOGYNAME():
    TECNOLOGY_NAME = []
    with open('nametechnique.txt', 'r') as file:
        TECNOLOGY_NAME = file.read().splitlines()

    for id in range(1, 501):
        randomTechnologyName = random.choice(TECNOLOGY_NAME)
        insertTechonologyName = 'INSERT INTO TECHNOLOGYNAME VALUES %s' % str((id, randomTechnologyName)) + ';'
        cur = connect.cursor()
        cur.execute(insertTechonologyName)
        connect.commit()
    print("Record inserted successfully")


def InsertTECHNIQUE():
    GUARANTEE = ['Да', 'Нет']

    for id in range(1, 501):
        randomYear = str(random.randint(2015, 2021))
        randomMouth = str(random.randint(1, 11))
        randomDay = str(random.randint(1, 27))
        randomYmd = str(randomYear + '-' + randomMouth + '-' + randomDay)
        randomAmount = random.randint(1, 30000)
        randomPrice = random.randint(1, 100000)
        randomGuarantee = random.choice(GUARANTEE)
        insertTechique = 'INSERT INTO TECHNIQUE VALUES %s' % str(
            (id, id, randomGuarantee, id, randomAmount, randomYmd, randomPrice)) + ';'
        cur = connect.cursor()
        cur.execute(insertTechique)
        connect.commit()
    print("Record inserted successfully")


def InsertSALE():
    for id in range(1, 501):
        randomAmount = random.randint(1, 5)
        randomDiscount = random.randint(1, 25)
        insertSale = 'INSERT INTO SALE VALUES %s' % str((id, id, randomAmount, randomDiscount)) + ';'
        cur = connect.cursor()
        cur.execute(insertSale)
        connect.commit()
    print("Record inserted successfully")
    connect.close()


def InsertCONSIGNMENT():
    for id in range(1, 501):
        randomYear = str(random.randint(2015, 2021))
        randomMouth = str(random.randint(1, 11))
        randomDay = str(random.randint(1, 27))
        randomYmd = str(randomYear + '-' + randomMouth + '-' + randomDay)
        insertConsignment = 'INSERT INTO CONSIGNMENT VALUES %s' % str((id, id, randomYmd)) + ';'
        cur = connect.cursor()
        cur.execute(insertConsignment)
        connect.commit()
    print("Record inserted successfully")


def InsertSUPPLIERS():
    PROVIDER = []
    with open('provider.txt', 'r') as file:
        PROVIDER = file.read().splitlines()
    for id in range(1, 501):
        randomProvider = random.choice(PROVIDER)
        insertSuppliers = 'INSERT INTO SUPPLIERS VALUES %s' % str((id, randomProvider)) + ';'
        cur = connect.cursor()
        cur.execute(insertSuppliers)
        connect.commit()
    print("Record inserted successfully")


def InsertACCOUNTS():
    for id in range(1, 501):
        randomYear = str(random.randint(2015, 2021))
        randomMouth = str(random.randint(1, 11))
        randomDay = str(random.randint(1, 27))
        randomYmd = str(randomYear + '-' + randomMouth + '-' + randomDay)
        randomSum = random.randint(1, 100000)
        randomDiscount = random.randint(1, 25)
        insertAccounts = 'INSERT INTO ACCOUNTS VALUES %s' % str((id, id, randomDiscount, randomYmd, randomSum)) + ';'
        cur = connect.cursor()
        cur.execute(insertAccounts)
        connect.commit()
    print("Record inserted successfully")


def InsertBUYERS():
    surnameMale = []
    with open('surnamemale.txt', 'r', encoding='utf-8', errors='ignore') as file:
        surnameMale = file.read().splitlines()
    nameMale = []
    with open('namemale.txt', 'r') as file:
        nameMale = file.read().splitlines()

    middlenameMale = []
    with open('middlenamemale.txt', 'r') as file:
        middlenameMale = file.read().splitlines()

    nameFemale = []
    with open('namefemale.txt', 'r') as file:
        nameFemale = file.read().splitlines()

    middlenameFemale = []
    with open('middlenamefemale.txt', 'r') as file:
       middlenameFemale = file.read().splitlines()

    for id in range(1, 501):
        randomPassId = random.randrange(1000, 9000)
        randomPassSer = random.randrange(100000, 900000)
        randomTel = str(random.randrange(1000000000, 9000000000))
        randomCredit = random.randrange(1000, 9000)
        if id % 2 == 0:
            randomSurNameMale = random.choice(surnameMale)
            randomNameMale = random.choice(nameMale)
            randomMiddleNameMale = random.choice(middlenameMale)
            insertBuyers = 'INSERT INTO BUYERS VALUES %s' % str((id, randomSurNameMale, randomNameMale,
                                                                 randomMiddleNameMale, randomPassId, randomPassSer,
                                                                 int('7' + randomTel), randomCredit)) + ';'
            cur = connect.cursor()
            cur.execute(insertBuyers)
            connect.commit()
        else:
            randomSurNameMale = random.choice(surnameMale)
            randomNameMale = random.choice(nameFemale)
            randomMiddleNameMale = random.choice(middlenameFemale)
            insertBuyers = 'INSERT INTO BUYERS VALUES %s' % str((id, randomSurNameMale + 'a', randomNameMale,
                                                                 randomMiddleNameMale, randomPassId, randomPassSer,
                                                                 int('7' + randomTel), randomCredit)) + ';'
            cur = connect.cursor()
            cur.execute(insertBuyers)
            connect.commit()
    print("Record inserted successfully")


CreateTABLES()
InsertTECHNOLOGYNAME()
InsertSUPPLIERS()
InsertCONSIGNMENT()
InsertBUYERS()
InsertACCOUNTS()
InsertTECHNIQUE()
InsertSALE()
