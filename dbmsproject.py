import mysql.connector

"""
create table userinfo(
	emailid varchar(60) not null primary key,
    passwd varchar(60) not null,
    fname varchar(40),
    lname varchar(40),
    country varchar(40),
    age int
);

create table inbox (
	from_eid varchar(60) not null,
    to_eid varchar(60) not null,
    tmstp timestamp not null,
    subj varchar(30),
    mailcontent varchar(1000),
	foreign key (from_eid) references userinfo(emailid),
    foreign key (to_eid) references userinfo(emailid)
);

create table trash (
	from_eid varchar(60) not null,
    to_eid varchar(60) not null,
    tmstp timestamp not null,
    subj varchar(30),
    mailcontent varchar(1000),
	foreign key (from_eid) references userinfo(emailid),
    foreign key (to_eid) references userinfo(emailid)
);

create table allmails(
	from_eid varchar(60) not null,
    to_eid varchar(60) not null,
    tmstp timestamp not null,
    subj varchar(30),
    mailcontent varchar(1000),
	foreign key (from_eid) references userinfo(emailid),
    foreign key (to_eid) references userinfo(emailid)
);


create table archieved(
	from_eid varchar(60) not null,
    to_eid varchar(60) not null,
    tmstp timestamp not null,
    subj varchar(30),
    mailcontent varchar(1000),
	foreign key (from_eid) references userinfo(emailid),
    foreign key (to_eid) references userinfo(emailid)
);
create table sent(
	from_eid varchar(60) not null,
    to_eid varchar(60) not null,
    tmstp timestamp not null,
    subj varchar(30),
    mailcontent varchar(1000),
	foreign key (from_eid) references userinfo(emailid),
    foreign key (to_eid) references userinfo(emailid)
);

"""


mydb = mysql.connector.connect(host="localhost",user="root",passwd = "dbms3050sql",database="emaildatabase")

mycursor = mydb.cursor()

# mycursor.execute("insert into userinfo values('nirbhaysharma@gmail.pom','password','nirbhay','sharma','india',26)")
# result = mycursor.fetchall()
# print(mycursor.rowcount)

# mydb.commit()



# for i in mycursor:
#     print(i[0])
def handlelogin():
    pass

s1 = """enter 0 for login
enter 1 for signup
enter 2 for exit"""
print(s1)
a = int(input('enter your choice : '))
if (a == 2):
    exit(0)
elif (a == 0):
    # login code
    eml = input('enter your email id: ')
    pas = input('enter your password: ')
    command= f"select * from userinfo where emailid = '{eml}' and passwd = '{pas}'"
    # print(command)
    mycursor.execute(command)
    cnt = 0
    l = []
    for i in mycursor:
        cnt += 1
        l.append(i)
    if (cnt == 0):
        print("user does not exists")
    else:
        print(f"welcome {l[0][2]} {l[0][3]}")
        handlelogin();
        
elif(a == 1):
    # signup code
    while(1):
        emlid = input('enter emailid: ')
        passwd = input('enter your password: ')
        fnam = input('enter first name: ')
        lnam = input('enter your last name: ')
        count = input('enter your country name: ')
        age = int(input('enter your age: '))
        command = f"select * from userinfo where emailid = '{emlid}'"
        finalcmd = f"insert into userinfo values ('{emlid}','{passwd}','{fnam}','{lnam}','{count}',{age})"
        mycursor.execute(command)
        cnt = 0
        for i in mycursor:
            cnt += 1
        if (cnt >= 1):
            print('user already exits with same username try enter another username')
            continue
        if (cnt == 0):
            mycursor.execute(finalcmd)
            mydb.commit()
            print('user registered')
            break
    

