#Question3-
#Problem Name - Mars Exploration
#HackerRank Link - https://www.hackerrank.com/challenges/validating-the-phone-number/problem?utm_source=chatgpt.com



#A space explorer's ship crashed on Mars! They send a series of SOS messages to Earth for help.
#Letters in some of the SOS messages are altered by cosmic radiation during transmission. Given the signal received by Earth as a string, , determine how many letters of the SOS message have been changed by radiation.

using namespace std;

/*
 * Complete the 'marsExploration' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts STRING s as parameter.
 */

int marsExploration(string s) {
    int count = 0;
    string expected = "SOS";
    
    for (int i = 0; i < s.length(); i++) {
        // Compare each character with the corresponding character in "SOS"
        if (s[i] != expected[i % 3]) {
            count++;
        }
    }
    
    return count;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    int result = marsExploration(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
