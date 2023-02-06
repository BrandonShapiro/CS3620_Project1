def get_user_input (prompt, options, functions, player):
  
  # initial values
  string_response = ""
  int_response = 100

  # print options
  print('\n')
  print("Options (Enter number or text):")
  count = 1
  for option in options:
    print("\t", count, "-", option)
    count += 1
  print()

  # get input
  string_response = input(prompt)
  
  # convert to int if needed
  if string_response.isdigit():
    int_response = int(string_response)

  # if input is invalid try again
  while(string_response not in options and int_response not in range(len(options) + 1)):
    print("Oops, that's not a valid option, try again " + player.getName() + "\n")

    print('\n')
    print("Options: ")
    count = 1
    for option in options:
      print("\t", count, "-", option)
      count += 1
    print()
    string_response = input(prompt)
    
    if string_response.isdigit():
      int_response = int(string_response)
    else:
      int_response = 0
  
  print()
  # run the function associated with the input value
  for count, item in enumerate(options, 1):
    if string_response == item or int_response == count:
      functions[count - 1](player)
