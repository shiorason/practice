#include <iostream>
#include <string>
using namespace std;

int main()
{
    string name;
    int tosi;

    cout << "こんにちは。私はコンピュータです。" << endl;
    cout << "あなたの名前を入力してください。" << endl;
    cin >> name;      //名前（文字列）の入力

    cout << name << "さん。よろしく。" << endl;

    cout << "ところで、" << name << "さん。失礼ですがお年はいくつですか？" << endl;
    cout << "(入力はかならず、半角の数字でお願いします。)" << endl;
    cin >> tosi;      //年齢（整数）の入力

    cout << "なるほど。" << tosi << "歳ですか。" << endl;
    cout << "私はもうすぐ2歳のマシンです。"<<endl;
}
