#include <iostream>
#include <string>
using namespace std;

int main()
{
    string name;
    int tosi;

    cout << "誰だお前は！" << endl;
    cin >> name;

    cout << "ふむ、、" << name << "というんだな！" << endl;

    cout << "ところで、" << name << "さん。失礼ですがお年はいくつですか？" << endl;
    cout << "(入力はかならず、半角の数字でお願いします。)" << endl;
    cin >> tosi;

    cout << "なるほど。" << tosi << "歳ですか。" << endl;
    cout << "私はもうすぐ2歳のマシンです。"<<endl;
}
