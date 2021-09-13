# Hashtables

Hashtables are a data structure that utilize key value pairs. This means every Node or Bucket has both a key, and a value.



## Challenge

Implement a Hashtable Class with the following methods:

add
Arguments: key, value
Returns: nothing
This method should hash the key, and add the key and value pair to the table, handling collisions as needed.

get
Arguments: key
Returns: Value associated with that key in the table

contains
Arguments: key
Returns: Boolean, indicating if the key exists in the table already.

hash
Arguments: key
Returns: Index in the collection for that key

## Approach & Efficiency

Big O:
 
Time O(n)
Space O(1)

## API

Add():

When adding a new key/value pair to a hashtable.

Find():

Takes in a key, gets the Hash, and goes to the index location specified. Once at the index location is found in the array, it is then the responsibility of the algorithm the iterate through the bucket and see if the key exists and return the value.

Contains() :

The Contains method will accept a key, and return a bool on if that key exists inside the hashtable. The best way to do this is to have the contains call the GetHash and check the hashtable if the key exists in the table given the index returned.

GetHash():
The GetHash will accept a key as a string, conduct the hash, and then return the index of the array where the key/value should be placed.