def login(user, password):
  if user == "deepa" and password == 1234:
    return "login successfully"
  return "Invalid Login"

print(login("deepa", 1234))