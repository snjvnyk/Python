import configparser

# create a new ConfigParser object
config = configparser.ConfigParser()

# add some users and their financial information to the config
config['user1'] = {'account_number': '1234567890',
                   'balance': '5000.00'}

config['user2'] = {'account_number': '0987654321',
                   'balance': '2500.00'}

# write the config to a file
with open('financial_data.ini', 'w') as configfile:
    config.write(configfile)

# read the config from the file
config.read('financial_data.ini')

# get a user's account number and balance
account_number = config['user1']['account_number']
balance = float(config['user1']['balance'])
print(f'User 1 has an account with number {account_number} and a balance of ${balance:.2f}.')

# get all the users and their balances
print('All users and their balances:')
for user in config.sections():
    balance = float(config[user]['balance'])
    print(f'{user}: ${balance:.2f}')
