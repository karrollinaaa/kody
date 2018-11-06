#include <iostream>
using namespace std;
int zlicz(char tab[]) {
int zlicz(char tb[])
{
    int i = 0;
    while(tab[i] != '\0') i++;
    
    while(tb[i] != '\0') i++;
    
    return i;
}
void wyswietl(char tekst[], int roz) {
    for(int i = 0; i < roz; i++) {
        cout << tekst[i];
        }
void wyswietl(char tb[], int roz)
{
    for (int i = 0; i < roz; i++)
    {
        cout << tb[i];
    }
}
void anagram(char tab[], roz) {
    int i = 0;
    for(i = roz - 1, i >= 0; i--) {
            
        }
void anagram(char tb[], int roz)
{
    for (int i = roz - 1; i >= 0; i--) {
        
        cout << tb[i];
    }
}
int main(int argc, char **argv)
{
    const int roz = 50;
	char tekst[roz];  
    cout << "Podaj jeden wyraz " ;
    cin.getline(tekst, roz);
    cout << "Wyraz: "  << tekst << endl;
    wyswietl(tekst, zlicz(tekst));
    const int rozmiar = 50;
    char tekst[rozmiar];
    
    cin.getline(tekst, rozmiar);
    
    wyswietl(tekst, cin.gcount());
    cout << endl;
    anagram(tekst, zlicz(tekst));
    
	return 0;
}

