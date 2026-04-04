def browser_history(commands):
    back_stack = [] # Stack to keep track of previously visited pages
    forward_stack = [] # Stack to keep track of pages that can be navigated forward to
    current_page = "Home" # Starting page
    output = [] # List to store the results of "CURRENT" commands

    for command in commands: # Process each command in the input list
        if command.startswith("VISIT"): # If the command is to visit a new page
            _, url = command.split(" ", 1) # Extract the URL from the command
            back_stack.append(current_page) # Push the current page onto the back stack before navigating to the new page
            current_page = url # Update the current page to the new URL
            forward_stack.clear() # Clear the forward stack since we are navigating to a new page, which invalidates any forward history
            
        elif command == "BACK": # If the command is to go back to the previous page
            if back_stack: # Check if there are pages in the back stack to go back to
                forward_stack.append(current_page) # Push the current page onto the forward stack before going back
                current_page = back_stack.pop() # Pop the last page from the back stack and set it as the current page
                
        elif command == "FORWARD": # If the command is to go forward to the next page
            if forward_stack: # Check if there are pages in the forward stack to go forward to
                back_stack.append(current_page) # Push the current page onto the back stack before going forward
                current_page = forward_stack.pop() # Pop the last page from the forward stack and set it as the current page
                
        elif command == "CURRENT": # If the command is to output the current page
            output.append(current_page) # Append the current page to the output list for "CURRENT" commands

    return output # Return the list of current pages for all "CURRENT" commands after processing all commands
