/* 

// 1. Iterate thru the array
// 2. If the current element - smallest element is still biggeer than the biggest difference that we have so far, then update the biggest difference
// 3. If the current element is smaller than the smallest element we have, update the smallest element.
// 4. After iterating through all elements in the array and performing operation on all elements, return the biggest difference.

TIME COMPLEXITY = O(N)
SPACE COMPLEXITY = O(1)

BRUTE FORCE = compare every single element with other elements and update the differences.
Time Complexity O(N^2) Space Complexity O(1)
*/

function riverRecords(arr) {

    // Find the initial biggest difference between two numbers in the arr
    biggest_difference = arr[1] - arr[0]

    // Initalize the smallest number in the array as the first element
    smallest_element = arr[0]

    for (let i = 1; i < arr.length; i++) {
        if (arr[i] - smallest_element > biggest_difference) biggest_difference = arr[i] - smallest_element

        if (arr[i] < smallest_element) smallest_element = arr[i]

    }
    return biggest_difference
}
