/*
Question boils down to if the paranthesis are valid or not.

1. Generate a ticketMap (Object) of left paranthesis as keys and right paranthesis as values.
    1.1 Reason for using map is fast access time O(1)
2. Iterate through each element in the tickets array
3. For each element in the array, perform the following operations
    3.1 Check if the elements of "(", "[", "{" are contained in that string if they do, push into Stack.
    3.2 If they are contained in the string, check the ticketMap values.
    3.2 If they exist in the ticketMap pop() from stack.
    3.3. If that position in Stack is empty ie length === 0; it's a valid paranthesis.

    3.4 Reason for using Stack. Operates as FIFO (First in First Out). Enables us to easily check if something is true by popping from the stack.

Optimal Solution:
Time Complexity = O(N)
Space Complexity = O(N)

Brute Force = Iterate thru every element and for the first element of that string, check the rest of the string if the opposite pair exists.
Time Complexity = O(N^2)
Space Complexity = O(1)

TradeOff between Time and Space.
*/

function validTickets(s) {
  // create a boolean list so that we can store multiple "YES", "NO" values.
  let booleanStack = [];

  // create an object. This allows fast access times of O(1)
  // Map allows us to access key and see if we can pop values.
  let ticketMap = {
    ")": "(",
    "]": "[",
    "}": "{",
  };

  // Creating a stack. A stack operates on FIFO (first in first out)
  // If our first element pases our Object test, we pop it from stack.
  // If the stack element is empty then its a valid ticket.
  let stack = [];
  for (let i = 0; i < s.length; i++) {
    //console.log(s[i])
    if (s[i] === "(" || s[i] === "[" || s[i] === "{") {
      stack.push(s[i]);
    } else {
      if (stack[stack.length - 1] === ticketMap[s[i]]) {
        stack.pop();
      } else booleanStack.push("NO");
    }
  }

  // the reason for the second for loop is that we have multiple "comma" seperated elements. We need to check if the element is empty of not. If it's empty then its a "YES" otherwise it's a "NO"

  for (let i = 0; i < stack.length; i++) {
    if (arr[i].length === 0) booleanStack.push("YES");
    else booleanStack.push("NO");
  }

  return booleanStack;
}
