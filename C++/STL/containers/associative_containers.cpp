#include <iostream>
#include <map>


using namespace std;

/*
  Map :
- Each element has a key value and a map value
- Key values are unique
*/

void mapTest() {
    
    cout << " ***** MAP TEST ***** " << endl;

    map<int,int> map1;
    

    map1.insert(pair<int,int>(1,10));
    map1.insert(pair<int,int>(2,20));
    map1.insert(pair<int,int>(3,30));
    map1.insert(pair<int,int>(4,40));
    map1.insert(pair<int,int>(6,50));
    map1.insert(pair<int,int>(7,60));

    cout << "Map 1" << endl;
    for(auto it = map1.begin(); it != map1.end(); ++it) {
        cout << '{' << it->first << ',' << it->second << '}' << ' ';
    }
    cout << endl;

    cout << "Copy first map in tmp map" << endl;
    cout << "Tmp map" << endl;
    map<int,int> tmp_map(map1.begin(), map1.end());
    for(auto it = tmp_map.begin(); it != tmp_map.end(); ++it) {
        cout << '{' << it->first << ',' << it->second << '}' << ' ';
    }
    cout << endl;

    cout << "Remove all elements up to key = 3" << endl;
    tmp_map.erase(tmp_map.begin(), tmp_map.find(3));
    for(auto it = tmp_map.begin(); it != tmp_map.end(); ++it) {
        cout << '{' << it->first << ',' << it->second << '}' << ' ';
    }
    cout << endl;

    cout << "Remove element with key = 3" << endl;
    tmp_map.erase(3);
    for(auto it = tmp_map.begin(); it != tmp_map.end(); ++it) {
        cout << '{' << it->first << ',' << it->second << '}' << ' ';
    }
    cout << endl;

}


int main() {

    mapTest();

    return 0;
}