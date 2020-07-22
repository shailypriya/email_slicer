#get user email address
email = input("What is your Email Address: ").strip()

#slice out username
user_name = email[:email.index("@")]

#slice domain name
domain_name = email[email.index("@")+1:]

#format message
output = "Your username is '{}' and your domain name is '{}'".format(user_name,domain_name)

#display the output
print(output)