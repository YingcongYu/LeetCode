// Design a HashMap without using any built-in hash table libraries.

// Implement the MyHashMap class:

// MyHashMap() initializes the object with an empty map.
// void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
// int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
// void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.


class MyHashMap {
    int[] values;

    public MyHashMap() {
        values = new int[1000001];
        Arrays.fill(values, -1);
    }
    
    public void put(int key, int value) {
        values[key] = value;
    }
    
    public int get(int key) {
        return values[key];
    }
    
    public void remove(int key) {
        values[key] = -1;
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */
