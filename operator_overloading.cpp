#include <iostream>

class Test {

    public:
        Test(int a = 0, int b = 0);

        Test operator+(Test t);
        std::pair<int,int> getPair();
    private:
        std::pair<int, int> m_pair;
        

};

Test::Test(int a, int b) {
    m_pair.first = a;
    m_pair.second =b;
}

std::pair<int,int> Test::getPair() {
    return this->m_pair;
}

Test Test::operator+(Test t) {

    Test result;
    result.m_pair.first = this->m_pair.first + t.m_pair.first;
    result.m_pair.second = this->m_pair.second + t.m_pair.second;

    return result;
}


int main() {

    Test test1(2,3);
    Test test2(8,5);
    Test test3 = test1 + test2;

    std::cout << '{' << test3.getPair().first << ',' << test3.getPair().second << '}' << std::endl;


    return 0;
}